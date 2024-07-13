import logging

from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import (
    EFirmwareId,
)

LOGGER = logging.getLogger("pyhausbus")

device_type_map = {
    EFirmwareId.ESP32: {
        int("0x65", 16): "LAN-RS485 Brückenmodul",
        int("0x18", 16): "6-fach Taster",
        int("0x19", 16): "4-fach Taster",
        int("0x1A", 16): "2-fach Taster",
        int("0x1B", 16): "1-fach Taster",
        int("0x1C", 16): "6-fach Taster Gira",
        int("0x20", 16): "32-fach IO",
        int("0x0C", 16): "16-fach Relais",
        int("0x08", 16): "8-fach Relais",
        int("0x10", 16): "22-fach UP-IO",
        int("0x28", 16): "8-fach Dimmer",
        int("0x30", 16): "2-fach RGB Dimmer",
        int("0x00", 16): "4-fach 0-10V Dimmer",
        int("0x01", 16): "4-fach 1-10V Dimmer",
    },
    EFirmwareId.HBC: {
        int("0x18", 16): "6-fach Taster",
        int("0x19", 16): "4-fach Taster",
        int("0x1A", 16): "2-fach Taster",
        int("0x1B", 16): "1-fach Taster",
        int("0x1C", 16): "6-fach Taster Gira",
        int("0x20", 16): "32-fach IO",
        int("0x0C", 16): "16-fach Relais",
        int("0x08", 16): "8-fach Relais",
        int("0x10", 16): "24-fach UP-IO",
        int("0x28", 16): "8-fach Dimmer",
        int("0x29", 16): "8-fach Dimmer",
        int("0x30", 16): "2-fach RGB Dimmer",
        int("0x00", 16): "4-fach 0-10V Dimmer",
        int("0x01", 16): "4-fach 1-10V Dimmer",
    },
    EFirmwareId.SD485: {
        int("0x28", 16): "24-fach UP-IO",
        int("0x1E", 16): "6-fach Taster",
        int("0x2E", 16): "6-fach Taster",
        int("0x2F", 16): "6-fach Taster",
        int("0x2B", 16): "4-fach 0-10V Dimmer",
        int("0x2C", 16): "4-fach Taster",
        int("0x2D", 16): "4-fach 1-10V Dimmer",
        int("0x2A", 16): "2-fach Taster",
        int("0x29", 16): "1-fach Taster",
    },
    EFirmwareId.AR8: {
        int("0x28", 16): "LAN Brückenmodul",
        int("0x30", 16): "8-fach Relais",
    },
    EFirmwareId.SD6: {
        int("0x14", 16): "Multitaster",
        int("0x1E", 16): "Multitaster",
    },
}


def get_device_type(firmware_id: EFirmwareId, type_id: int) -> str:
    """Get device type from firmware ID and type ID."""
    firmware_model_id = device_type_map.get(firmware_id, {})
    if len(firmware_model_id) == 0:
        return "Controller"
    else:
        return firmware_model_id.get(type_id, "Controller")
