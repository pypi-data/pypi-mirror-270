import argparse
import os
import sys
from importlib.metadata import version
from typing import Iterable, Literal

import IPython
from IPython.terminal.ipapp import TerminalIPythonApp
from IPython.terminal.prompts import Prompts, Token

from bec_ipython_client.beamline_mixin import BeamlineMixin
from bec_ipython_client.bec_magics import BECMagics
from bec_ipython_client.callbacks.ipython_live_updates import IPythonLiveUpdates
from bec_ipython_client.signals import ScanInterruption, SigintHandler
from bec_lib import ServiceConfig, bec_logger, plugin_helper
from bec_lib.alarm_handler import AlarmBase
from bec_lib.callback_handler import EventType
from bec_lib.client import BECClient
from bec_lib.connector import ConnectorBase

logger = bec_logger.logger


class BECIPythonClient:
    def __init__(
        self,
        config: ServiceConfig = None,
        connector_cls: ConnectorBase = None,
        wait_for_server=True,
        forced=False,
    ) -> None:
        self._client = BECClient(config, connector_cls, wait_for_server, forced, parent=self)
        self._ip = IPython.get_ipython()
        self.started = False
        self._sighandler = None
        self._beamline_mixin = None
        self._exit_event = None
        self._exit_handler_thread = None
        self.live_updates = None
        self.fig = None
        self._client.callbacks.register(
            event_type=EventType.NAMESPACE_UPDATE, callback=self._update_namespace_callback
        )
        self._client.load_high_level_interface("bec_hli")

    def __getattr__(self, name):
        return getattr(self._client, name)

    def __dir__(self) -> Iterable[str]:
        return dir(self._client) + dir(self.__class__)

    def __str__(self) -> str:
        return "BECIPythonClient\n\nTo get a list of available commands, type `bec.show_all_commands()`"

    def start(self):
        """start the client"""
        if self.started:
            return
        self._client.start()
        self._sighandler = SigintHandler(self)
        self._beamline_mixin = BeamlineMixin()
        self.live_updates = IPythonLiveUpdates(self)
        self._configure_ipython()
        self.started = True

    def bl_show_all(self):
        self._beamline_mixin.bl_show_all()

    def _set_ipython_prompt_scan_number(self, scan_number: int):
        if self._ip:
            self._ip.prompts.scan_number = scan_number + 1

    def _configure_ipython(self):

        if self._ip is None:
            return

        self._ip.prompts = BECClientPrompt(ip=self._ip, client=self._client, username="demo")
        self._load_magics()
        self._ip.events.register("post_run_cell", log_console)
        self._ip.set_custom_exc((Exception,), _ip_exception_handler)  # register your handler
        # represent objects using __str__, if overwritten, otherwise use __repr__
        self._ip.display_formatter.formatters["text/plain"].for_type(
            object,
            lambda o, p, cycle: o.__str__ is object.__str__ and p.text(repr(o)) or p.text(str(o)),
        )

    def _update_namespace_callback(self, action: Literal["add", "remove"], ns_objects: dict):
        """Callback to update the global namespace of ipython.

        Within BEC, the callback is triggered by the CallbackHandler when
        the namespace changes, e.g. load_high_level_interface, load_user_script, etc.

        Args:
            action (Literal["add", "remove"]): action to perform
            ns_objects (dict): objects to add or remove

        """
        if action == "add":
            for name, obj in ns_objects.items():
                self._ip.user_global_ns[name] = obj
        elif action == "remove":
            for name, obj in ns_objects.items():
                self._ip.user_global_ns.pop(name)

    def _set_error(self):
        if self._ip is not None:
            self._ip.prompts.status = 0

    def _set_busy(self):
        if self._ip is not None:
            self._ip.prompts.status = 1

    def _set_idle(self):
        if self._ip is not None:
            self._ip.prompts.status = 2

    def _load_magics(self):
        magics = BECMagics(self._ip, self._client)
        self._ip.register_magics(magics)

    def shutdown(self):
        """shutdown the client and all its components"""
        if self.fig:
            self.fig.close()
        self._client.shutdown()


def _ip_exception_handler(self, etype, evalue, tb, tb_offset=None):
    if issubclass(etype, (AlarmBase, ScanInterruption)):
        print(f"\x1b[31m BEC alarm:\x1b[0m: {evalue}")
        return
    self.showtraceback((etype, evalue, tb), tb_offset=None)  # standard IPython's printout


class BECClientPrompt(Prompts):
    def __init__(self, ip, username, client, status=0):
        self._username = username
        self.client = client
        self.status = status
        super().__init__(ip)

    def in_prompt_tokens(self, cli=None):
        if self.status == 0:
            status_led = Token.OutPromptNum
        elif self.status == 1:
            status_led = Token.PromptNum
        else:
            status_led = Token.Prompt
        try:
            next_scan_number = str(self.client.queue.next_scan_number)
        except Exception:
            next_scan_number = "?"
        return [
            (status_led, "\u2022"),
            (Token.Prompt, " " + self.username),
            (Token.Prompt, " ["),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, "/"),
            (Token.PromptNum, next_scan_number),
            (Token.Prompt, "] "),
            (Token.Prompt, "❯❯ "),
        ]

    @property
    def username(self):
        """current username"""
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


def log_console(execution_info):
    """log the console input"""
    logger.log("CONSOLE_LOG", f"{execution_info.info.raw_cell}")


# pylint: disable=wrong-import-position
# pylint: disable=protected-access
# pylint: disable=unused-import
# pylint: disable=ungrouped-imports

main_dict = {}

sys.modules["bec_ipython_client.main"] = sys.modules[
    __name__
]  # properly register module when file is executed directly, like in test


def main():
    """
    Main function to start the BEC IPython client.
    """

    available_plugins = plugin_helper.get_ipython_client_startup_plugins(state="pre")

    parser = argparse.ArgumentParser(
        prog="BEC IPython client", description="BEC command line interface"
    )
    parser.add_argument("--version", action="store_true", default=False)
    parser.add_argument("--nogui", action="store_true", default=False)
    parser.add_argument("--config", action="store", default=None)
    parser.add_argument("--dont-wait-for-server", action="store_true", default=False)
    parser.add_argument("--post-startup-file", action="store", default=None)

    for plugin in available_plugins.values():
        if hasattr(plugin["module"], "extend_command_line_args"):
            plugin["module"].extend_command_line_args(parser)

    args, left_args = parser.parse_known_args()

    # remove already parsed args from command line args
    sys.argv = sys.argv[:1] + left_args

    if args.version:
        print(f"BEC IPython client: {version('bec_ipython_client')}")
        sys.exit(0)

    config_file = args.config
    if config_file:
        if not os.path.isfile(config_file):
            raise FileNotFoundError("Config file not found.")
        print("Using config file: ", config_file)
        config = ServiceConfig(config_file)

    if available_plugins and "config" not in locals():
        # check if pre-startup.py script exists
        for plugin in available_plugins.values():
            if hasattr(plugin["module"], "get_config"):
                config = plugin.get_config()
                break

    # check if config was defined in pre-startup.py
    if "config" not in locals():
        config = ServiceConfig()

    main_dict["config"] = config
    main_dict["args"] = args
    main_dict["wait_for_server"] = not args.dont_wait_for_server
    main_dict["startup_file"] = args.post_startup_file

    app = TerminalIPythonApp()
    app.interact = True
    app.initialize(argv=["-i", os.path.join(os.path.dirname(__file__), "bec_startup.py")])

    try:
        app.start()
    finally:
        if "bec" in main_dict:
            # bec object is inserted into main_dict by bec_startup
            main_dict["bec"].shutdown()


if __name__ == "__main__":
    main()
