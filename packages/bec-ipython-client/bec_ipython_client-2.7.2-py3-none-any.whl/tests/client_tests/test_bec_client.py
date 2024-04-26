import subprocess
import sys
from unittest import mock

import IPython
import pytest

from bec_ipython_client import BECIPythonClient, main
from bec_lib import RedisConnector, ServiceConfig


def test_bec_entry_point_globals_and_post_startup(tmpdir):  # , capfd):
    file_to_execute = tmpdir / "post_startup.py"
    with open(file_to_execute, "w") as f:
        f.write(
            """
try:
  completer=get_ipython().Completer
  import sys
  print(completer.all_completions('bec.'), flush=True)
  print(completer.all_completions('BECIP'), flush=True)
finally:
  import os
  import signal
  os.kill(os.getpid(), signal.SIGTERM)
"""
        )
    p = subprocess.Popen(
        [
            sys.executable,
            main.__file__,
            "--nogui",
            "--dont-wait-for-server",
            "--post-startup-file",
            file_to_execute,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    output, _ = p.communicate()
    assert "bec.device_manager" in output  # just one of many completions
    assert (
        "BECIPythonClient" not in output
    )  # just to ensure something we don't want is really not there


def test_bec_load_hli_tab_completion(tmpdir):
    """Test that bec hli is loaded and tab completion in the ipython client works"""
    file_to_execute = tmpdir / "post_startup.py"
    with open(file_to_execute, "w") as f:
        f.write(
            """
try:
  completer=get_ipython().Completer
  import sys
  print(completer.all_completions('umv'), flush=True)
  print(completer.all_completions('mv'), flush=True)
finally:
  import os
  import signal
  os.kill(os.getpid(), signal.SIGTERM)
"""
        )
    p = subprocess.Popen(
        [
            sys.executable,
            main.__file__,
            "--nogui",
            "--dont-wait-for-server",
            "--post-startup-file",
            file_to_execute,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    output, _ = p.communicate()
    assert "umvr" in output
    assert "umv" in output
    assert "mv" in output
    assert "mvr" in output


def test_ipython_device_completion(bec_client_mock):
    client = bec_client_mock
    # disable history saving (which runs in a separate thread)
    with mock.patch("IPython.core.history.HistoryManager.enabled", False):
        shell = IPython.terminal.interactiveshell.TerminalInteractiveShell.instance()
        shell.user_ns["dev"] = client.device_manager.devices
        completer = IPython.get_ipython().Completer
        assert "dev.samx" in completer.all_completions("dev.sa")
        assert len(completer.all_completions("dev.sa")) == 3


def test_ipython_device_completion_property_access(bec_client_mock):
    client = bec_client_mock
    # disable history saving (which runs in a separate thread)
    with mock.patch("IPython.core.history.HistoryManager.enabled", False):
        shell = IPython.terminal.interactiveshell.TerminalInteractiveShell.instance()
        shell.user_ns["dev"] = client.device_manager.devices
        completer = IPython.get_ipython().Completer
        assert "dev.samx.dummy_controller.some_var" in completer.all_completions(
            "dev.samx.dummy_controller.som"
        )


@pytest.fixture
def service_config():
    return ServiceConfig(
        redis={"host": "localhost", "port": 5000},
        scibec={"host": "localhost", "port": 5001},
        mongodb={"host": "localhost", "port": 50002},
    )


@pytest.fixture
def ipython_client(service_config):
    client = BECIPythonClient(
        config=service_config,
        connector_cls=mock.MagicMock(spec=RedisConnector),
        wait_for_server=False,
    )
    yield client
    client.shutdown()
    client._client._reset_singleton()


def test_bec_ipython_client_start(service_config):
    client = BECIPythonClient(
        config=service_config,
        connector_cls=mock.MagicMock(spec=RedisConnector),
        wait_for_server=True,
    )
    try:
        with mock.patch.object(client._client, "wait_for_service") as wait_for_service:
            with mock.patch.object(client, "_configure_ipython") as configure_ipython:
                with mock.patch.object(client, "_load_scans"):
                    client.start()
                    configure_ipython.assert_called_once()
                    assert mock.call("ScanBundler", mock.ANY) in wait_for_service.call_args_list
                    assert mock.call("ScanServer", mock.ANY) in wait_for_service.call_args_list
                    assert mock.call("DeviceServer", mock.ANY) in wait_for_service.call_args_list
                    assert client.started
    finally:
        client.shutdown()
        client._client._reset_singleton()


def test_bec_update_username_space(ipython_client):
    client = ipython_client
    with mock.patch.object(client, "wait_for_service") as wait_for_service:
        with mock.patch.object(client, "_configure_ipython") as configure_ipython:
            with mock.patch.object(client, "_load_scans"):
                with mock.patch.object(client, "_ip") as mock_ipy:
                    client.start()
                    mock_ipy.user_global_ns = {}
                    my_object = object()
                    client._update_namespace_callback(action="add", ns_objects={"mv": my_object})
                    assert "mv" in mock_ipy.user_global_ns
                    assert mock_ipy.user_global_ns["mv"] == my_object
                    client._update_namespace_callback(action="remove", ns_objects={"mv": my_object})
                    assert "mv" not in mock_ipy.user_global_ns


def test_bec_ipython_client_start_without_bec_services(ipython_client):
    client = ipython_client
    with mock.patch.object(client, "wait_for_service") as wait_for_service:
        with mock.patch.object(client, "_configure_ipython") as configure_ipython:
            with mock.patch.object(client, "_load_scans"):
                client.start()
                configure_ipython.assert_called_once()
                wait_for_service.assert_not_called()
