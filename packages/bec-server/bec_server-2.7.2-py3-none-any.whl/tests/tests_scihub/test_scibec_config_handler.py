# pylint: skip-file
import os
from unittest import mock

import pytest
import yaml
from fastjsonschema import JsonSchemaException
from test_scibec_connector import SciBecMock, SciHubMock

import bec_lib
from bec_lib import DeviceBase, messages
from bec_lib.bec_errors import DeviceConfigError
from bec_lib.device import OnFailure, ReadoutPriority
from bec_server.scihub import SciHub
from bec_server.scihub.scibec import ConfigHandler, SciBecConnector

dir_path = os.path.dirname(bec_lib.__file__)


@pytest.fixture()
def config_handler(SciHubMock):
    with mock.patch("bec_server.scihub.scibec.scibec_connector.os.path.exists", return_value=False):
        scibec_connector = SciBecConnector(SciHubMock, SciHubMock.connector)
    with mock.patch.object(scibec_connector, "_start_config_request_handler"):
        with mock.patch.object(scibec_connector, "_start_metadata_handler"):
            with mock.patch.object(scibec_connector, "_start_scibec_account_update"):
                scibec_connector.scibec = None
                yield scibec_connector.config_handler
                scibec_connector.shutdown()


@pytest.fixture
def available_keys_fixture(test_config_yaml):
    config_content = test_config_yaml
    config_keys_from_config = []
    for dev_config in config_content.values():
        for k in dev_config.keys():
            config_keys_from_config.append(k)
    config_keys_from_config = set(config_keys_from_config)
    # remove enabled and deviceClass, as it is not handled from config_handler
    config_keys_from_config.remove("enabled")
    config_keys_from_config.remove("deviceClass")
    return config_keys_from_config


def test_parse_config_request_update(config_handler):
    msg = messages.DeviceConfigMessage(
        action="update", config={"samx": {"enabled": True}}, metadata={}
    )
    with mock.patch.object(config_handler, "_update_config") as update_config, mock.patch.object(
        config_handler.device_manager, "check_request_validity"
    ) as req_validity:
        config_handler.parse_config_request(msg)
        req_validity.assert_called_once_with(msg)
        update_config.assert_called_once_with(msg)


def test_parse_config_request_reload(config_handler):
    msg = messages.DeviceConfigMessage(action="reload", config={}, metadata={})
    with mock.patch.object(config_handler, "_reload_config") as reload_config, mock.patch.object(
        config_handler.device_manager, "check_request_validity"
    ) as req_validity:
        config_handler.parse_config_request(msg)
        req_validity.assert_called_once_with(msg)
        reload_config.assert_called_once_with(msg)


def test_parse_config_request_set(config_handler):
    msg = messages.DeviceConfigMessage(
        action="set", config={"samx": {"enabled": True}}, metadata={}
    )
    with mock.patch.object(config_handler, "_set_config") as set_config, mock.patch.object(
        config_handler.device_manager, "check_request_validity"
    ) as req_validity:
        config_handler.parse_config_request(msg)
        req_validity.assert_called_once_with(msg)
        set_config.assert_called_once_with(msg)


def test_parse_config_request_exception(config_handler):
    msg = messages.DeviceConfigMessage(
        action="update", config={"samx": {"enabled": True}}, metadata={}
    )
    with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
        with mock.patch("bec_server.scihub.scibec.config_handler.traceback.format_exc") as exc:
            with mock.patch.object(config_handler, "_update_config", side_effect=AttributeError()):
                config_handler.parse_config_request(msg)
                req_reply.assert_called_once_with(accepted=False, error_msg=exc(), metadata={})


def test_config_handler_reload_config(config_handler):
    msg = messages.DeviceConfigMessage(action="reload", config={}, metadata={})
    with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
        with mock.patch.object(config_handler, "send_config") as send:
            config_handler.parse_config_request(msg)
            send.assert_called_once_with(msg)


### Commented out as config updates on scibec are not supported yet

# def test_config_handler_reload_config_with_scibec(SciHubMock):
#     scibec_connector = SciBecMock
#     config_handler = scibec_connector.config_handler
#     msg = messages.DeviceConfigMessage(action="reload", config={}, metadata={})
#     with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
#         with mock.patch.object(scibec_connector, "scibec"):
#             with mock.patch.object(scibec_connector, "update_session") as update_session:
#                 with mock.patch.object(config_handler, "send_config") as send:
#                     config_handler.parse_config_request(msg)
#                     send.assert_called_once_with(msg)
#                     update_session.assert_called_once()


@pytest.mark.parametrize(
    "config, expected",
    [
        ({"samx": {"enabled": True}}, {"name": "samx", "enabled": True}),
        (
            {"samx": {"enabled": True, "deviceConfig": None}},
            {"name": "samx", "enabled": True, "deviceConfig": {}},
        ),
    ],
)
def test_config_handler_set_config(config_handler, config, expected):
    msg = messages.DeviceConfigMessage(action="set", config=config, metadata={"RID": "12345"})
    with mock.patch.object(config_handler.validator, "validate_device") as validator:
        with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
            with mock.patch.object(
                config_handler,
                "_wait_for_device_server_update",
                return_value=(True, mock.MagicMock()),
            ) as wait:
                with mock.patch.object(config_handler, "send_config") as send_config:
                    config_handler._set_config(msg)
                    req_reply.assert_called_once_with(
                        accepted=True,
                        error_msg=None,
                        metadata={"RID": "12345", "updated_config": True},
                    )
                    validator.assert_called_once_with(expected)
                    send_config.assert_called_once_with(
                        messages.DeviceConfigMessage(
                            action="reload",
                            config={},
                            metadata={"RID": "12345", "updated_config": True},
                        )
                    )


def test_config_handler_set_invalid_config_raises(config_handler):
    msg = messages.DeviceConfigMessage(
        action="set", config={"samx": {"status": {"enabled": True}}}, metadata={"RID": "12345"}
    )
    with pytest.raises(JsonSchemaException):
        with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
            config_handler._set_config(msg)
            req_reply.assert_called_once_with(
                accepted=True, error_msg=None, metadata={"RID": "12345"}
            )


### Commented out as config updates on scibec are not supported yet

# def test_config_handler_set_config_with_scibec(SciHubMock):
#     scibec_connector = SciBecMock
#     config_handler = scibec_connector.config_handler
#     msg = messages.DeviceConfigMessage(
#         action="set", config={"samx": {"enabled": True}}, metadata={}
#     )
#     scibec_connector.scibec_info = {"beamline": {"info": [], "activeExperiment": "12345"}}
#     with mock.patch.object(scibec_connector, "scibec") as scibec:
#         with mock.patch.object(config_handler, "send_config_request_reply") as req_reply:
#             with mock.patch.object(scibec_connector, "update_session") as update_session:
#                 config_handler._set_config(msg)
#                 scibec.set_session_data.assert_called_once_with(
#                     "12345", {"samx": {"enabled": True}}
#                 )
#                 req_reply.assert_called_once_with(accepted=True, error_msg=None, metadata={})
#                 update_session.assert_called_once()


def test_config_handler_update_config(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={})
    msg = messages.DeviceConfigMessage(
        action="update", config={"samx": {"enabled": True}}, metadata={}
    )
    with mock.patch.object(
        config_handler, "_update_device_config", return_value=True
    ) as update_device_config:
        with mock.patch.object(config_handler, "update_config_in_redis") as update_config_in_redis:
            with mock.patch.object(config_handler, "send_config") as send_config:
                with mock.patch.object(
                    config_handler, "send_config_request_reply"
                ) as send_config_request_reply:
                    config_handler._update_config(msg)
                    update_device_config.assert_called_once_with(dev["samx"], {"enabled": True})
                    update_config_in_redis.assert_called_once_with(dev["samx"])

                    send_config.assert_called_once_with(msg)
                    send_config_request_reply.assert_called_once_with(
                        accepted=True, error_msg=None, metadata={}
                    )


def test_config_handler_update_config_not_updated(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={})
    msg = messages.DeviceConfigMessage(
        action="update", config={"samx": {"enabled": True}}, metadata={}
    )
    with mock.patch.object(
        config_handler, "_update_device_config", return_value=False
    ) as update_device_config:
        with mock.patch.object(config_handler, "update_config_in_redis") as update_config_in_redis:
            with mock.patch.object(config_handler, "send_config") as send_config:
                with mock.patch.object(
                    config_handler, "send_config_request_reply"
                ) as send_config_request_reply:
                    config_handler._update_config(msg)
                    update_device_config.assert_called_once_with(dev["samx"], {"enabled": True})
                    update_config_in_redis.assert_not_called()

                    send_config.assert_not_called()
                    send_config_request_reply.assert_not_called()


def test_config_handler_update_device_config_enable(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={})
    with mock.patch.object(config_handler, "_update_device_server") as update_dev_server:
        with mock.patch.object(
            config_handler, "_wait_for_device_server_update", return_value=(True, mock.MagicMock())
        ) as wait:
            with mock.patch("bec_server.scihub.scibec.config_handler.uuid") as uuid:
                device = dev["samx"]
                rid = str(uuid.uuid4())
                config_handler._update_device_config(device, {"enabled": True})
                # mock doesn't copy the data, hence the popped result:
                update_dev_server.assert_called_once_with(rid, {device.name: {}})
                wait.assert_called_once_with(rid)


def test_config_handler_update_device_config_deviceConfig(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={"deviceConfig": {}})
    with mock.patch.object(config_handler, "_update_device_server") as update_dev_server:
        with mock.patch.object(
            config_handler, "_wait_for_device_server_update", return_value=(True, mock.MagicMock())
        ) as wait:
            with mock.patch("bec_server.scihub.scibec.config_handler.uuid") as uuid:
                device = dev["samx"]
                rid = str(uuid.uuid4())
                config_handler._update_device_config(
                    device, {"deviceConfig": {"something": "to_update"}}
                )
                # mock doesn't copy the data, hence the popped result:
                update_dev_server.assert_called_once_with(rid, {device.name: {}})
                wait.assert_called_once_with(rid)
                assert dev.samx._config == {"deviceConfig": {"something": "to_update"}}


def test_config_handler_update_device_config_misc(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={})
    with mock.patch.object(config_handler, "_validate_update") as validate_update:
        device = dev["samx"]
        config_handler._update_device_config(device, {"readOnly": True})
        validate_update.assert_called_once_with({"readOnly": True})


def test_config_handler_update_device_config_raise(config_handler):
    dev = config_handler.device_manager.devices
    dev.samx = DeviceBase(name="samx", config={})
    with mock.patch.object(config_handler, "_validate_update") as validate_update:
        device = dev["samx"]
        with pytest.raises(DeviceConfigError):
            config_handler._update_device_config(device, {"doesnt_exist": False})


def test_config_handler_update_device_config_available_keys(config_handler, available_keys_fixture):
    for available_key in available_keys_fixture:
        dev = config_handler.device_manager.devices
        if available_key in ["deviceConfig", "userParameter"]:
            init = {"something": "to_update"}
            dev.samx = DeviceBase(name="samx", config={available_key: init})
        elif available_key in ["softwareTrigger", "readOnly"]:
            init = True
            dev.samx = DeviceBase(name="samx", config={available_key: init})
        elif available_key in ["readoutPriority"]:
            init = ReadoutPriority.BASELINE
            dev.samx = DeviceBase(name="samx", config={available_key: init})
        elif available_key in ["onFailure"]:
            init = OnFailure.BUFFER
            dev.samx = DeviceBase(name="samx", config={available_key: init})
        elif available_key in ["deviceTags"]:
            init = ["something"]
            dev.samx = DeviceBase(name="samx", config={available_key: init})
        else:
            dev.samx = DeviceBase(name="samx", config={})
        with mock.patch.object(config_handler, "_update_device_server") as update_dev_server:
            with mock.patch.object(
                config_handler,
                "_wait_for_device_server_update",
                return_value=(True, mock.MagicMock()),
            ) as wait:
                with mock.patch("bec_server.scihub.scibec.config_handler.uuid") as uuid:
                    device = dev["samx"]
                    rid = str(uuid.uuid4())
                    if available_key in ["deviceConfig", "userParameter"]:
                        update = {"something": "to_update"}
                        config_handler._update_device_config(device, {available_key: update})
                    elif available_key in ["softwareTrigger", "readOnly"]:
                        update = True
                        config_handler._update_device_config(device, {available_key: update})
                    elif available_key in ["readoutPriority"]:
                        update = ReadoutPriority.MONITORED
                        config_handler._update_device_config(device, {available_key: update})
                    elif available_key in ["readoutPriority"]:
                        update = OnFailure.RETRY
                        config_handler._update_device_config(device, {available_key: update})
                    elif available_key in ["deviceTags"]:
                        update = ["something"]
                        config_handler._update_device_config(device, {available_key: update})
                    else:
                        update = ""
                        config_handler._update_device_config(device, {available_key: update})
                    # mock doesn't copy the data, hence the popped result:
                    if available_key == "deviceConfig":
                        update_dev_server.assert_called_once_with(rid, {device.name: {}})
                        wait.assert_called_once_with(rid)
                    assert dev.samx._config == {available_key: update}


def test_config_handler_wait_for_device_server_update(config_handler):
    RID = "12345"
    with mock.patch.object(config_handler.connector, "get") as mock_get:
        mock_get.side_effect = [
            None,
            None,
            None,
            messages.RequestResponseMessage(accepted=True, message=""),
        ]
        config_handler._wait_for_device_server_update(RID)


def test_config_handler_wait_for_device_server_update_timeout(config_handler):
    RID = "12345"
    with mock.patch.object(config_handler.connector, "get", return_value=None) as mock_get:
        with pytest.raises(TimeoutError):
            config_handler._wait_for_device_server_update(RID, timeout_time=0.1)
            mock_get.assert_called()
