import os
import sys

import numpy as np  # not needed but always nice to have

from bec_ipython_client.main import BECIPythonClient as _BECIPythonClient
from bec_ipython_client.main import main_dict as _main_dict
from bec_lib import RedisConnector as _RedisConnector
from bec_lib import bec_logger as _bec_logger
from bec_lib import plugin_helper

try:
    from bec_widgets.cli import BECFigure as _BECFigure
except ImportError:
    _BECFigure = None

logger = _bec_logger.logger

bec = _BECIPythonClient(
    _main_dict["config"], _RedisConnector, wait_for_server=_main_dict["wait_for_server"]
)
_main_dict["bec"] = bec

if not _main_dict["args"].nogui and _BECFigure is not None:
    fig = bec.fig = _BECFigure()
    fig.show()

try:
    bec.start()
except Exception:
    sys.excepthook(*sys.exc_info())
else:

    dev = bec.device_manager.devices
    scans = bec.scans

    _available_plugins = plugin_helper.get_ipython_client_startup_plugins(state="post")
    if _available_plugins:
        for name, plugin in _available_plugins.items():
            logger.success(f"Loading plugin: {plugin['source']}")
            base = os.path.dirname(plugin["module"].__file__)
            with open(os.path.join(base, "post_startup.py"), "r", encoding="utf-8") as file:
                # pylint: disable=exec-used
                exec(file.read())

    else:
        bec._ip.prompts.status = 1

if _main_dict["startup_file"]:
    with open(_main_dict["startup_file"], "r", encoding="utf-8") as file:
        # pylint: disable=exec-used
        exec(file.read())
