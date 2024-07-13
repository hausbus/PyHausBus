import logging
import time
import traceback

from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import (
    EFirmwareId,
)

LOGGER = logging.getLogger("pyhausbus")

HOMESERVER_DEVICE_ID: int = 9998
HOMESERVER_OBJECT_ID: int = (HOMESERVER_DEVICE_ID << 16) + (0 << 8) + 1

UDP_PORT = 5855


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


def getObjectId(deviceId: int, classId: int, instanceId: int) -> int:
    return (deviceId << 16) + (classId << 8) + instanceId


def bytesToDWord(data: bytearray, offset) -> int:
    try:
        result = 0
        result += data[offset[0]] & 0xFF
        offset[0] += 1

        result += (data[offset[0]] & 0xFF) * 256
        offset[0] += 1

        result += (data[offset[0]] & 0xFF) * 65536
        offset[0] += 1

        result += (data[offset[0]] & 0xFF) * 16777216
        offset[0] += 1

        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return 0


def bytesToWord(data: bytearray, offset) -> int:
    try:
        result = 0
        result += data[offset[0]] & 0xFF
        offset[0] += 1

        result += (data[offset[0]] & 0xFF) * 256
        offset[0] += 1

        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return 0


def bytesToInt(data: bytearray, offset) -> int:
    try:
        if len(data) <= offset[0]:
            return 0
        result = data[offset[0]] & 0xFF
        offset[0] += 1
        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return 0


def bytesToString(data: bytearray, offset) -> str:
    try:
        result = ""
        for i in range(offset[0], len(data)):
            offset[0] += 1
            if data[i] == 0:
                break

            result += chr(data[i])
        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return ""


def bytesToDebugString(message: bytearray) -> str:
    result = ""
    for byte in message:
        if result != "":
            result = result + ", "
        result = result + hex(byte)
    return result


def getInstanceId(objectId) -> int:
    return (objectId) & 0xFF


def getDeviceId(objectId) -> int:
    return ((objectId >> 24) & 0xFF) * 256 + ((objectId >> 16) & 0xFF)


def getClassId(objectId) -> int:
    return (objectId >> 8) & 0xFF


def formatObjectId(objectId) -> str:
    result = "[DeviceId: " + str(getDeviceId(objectId))
    result += ", ClassId: " + str(getClassId(objectId))
    result += ", Instance: " + str(getInstanceId(objectId)) + "]"
    return result


def getClockIndependMillis():
    return time.perf_counter() * 1000


def setBit(is_set: bool, bit: int, value: int) -> int:
    if is_set:
        value |= 1 << bit
    else:
        value &= ~(1 << bit)
    return value


def isBitSet(bit: int, value: int) -> bool:
    return ((value >> bit) & 1) > 0


def bytesToBlob(data: bytearray, offset) -> bytearray:
    try:
        result = bytearray(len(data) - offset[0])
        result[:] = data[offset[0] :]
        offset[0] = offset[0] + len(data)
        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return 0


def dWordToBytes(value: int) -> bytearray:
    result = bytearray(4)
    result[0] = value & 0xFF
    result[1] = (value >> 8) & 0xFF
    result[2] = (value >> 16) & 0xFF
    result[3] = (value >> 24) & 0xFF
    return result


def addWord(value: int, inOutList):
    inOutList.append(value & 0xFF)
    inOutList.append((value >> 8) & 0xFF)


def addDword(value: int, inOutList):
    inOutList.append(value & 0xFF)
    inOutList.append((value >> 8) & 0xFF)
    inOutList.append((value >> 16) & 0xFF)
    inOutList.append((value >> 24) & 0xFF)


def wordToBytes(value: int) -> bytearray:
    result = bytearray(2)
    result[0] = value & 0xFF
    result[1] = (value >> 8) & 0xFF
    return result


def bytesToSInt(data: bytearray, offset) -> int:
    result = data[offset[0]] & 0xFF
    offset[0] += 1
    if result > 127:
        result -= 256
    return result


def formatBytes(
    data: bytearray, offset: int = 0, length: int = -1, asHex: bool = True
) -> str:
    if length == -1:
        length = len(data)

        if data == None:
            return "NULL"

        result = ""

        for i in range(offset, length):
            if asHex:
                result += "0x" + hex(data[i])
            else:
                result += data[i] & 0xFF
        return result


def bytesToList(data: bytearray, offset):
    try:
        result = bytearray()
        offsetStart = offset[0]
        for i in range(offsetStart, len(data), 2):
            key = data[i] & 0xFF
            value = data[i + 1] & 0xFF
            result.append(key)
            result.append(value)
            offset[0] += 2
        return result
    except Exception as err:
        LOGGER.error(err, exc_info=True, stack_info=True)
        return bytearray()


def get_device_type(firmware_id: EFirmwareId, type_id: int) -> str:
    """Get device type from firmware ID and type ID."""
    firmware_model_id = device_type_map.get(firmware_id, {})
    if len(firmware_model_id) == 0:
        return "Controller"
    else:
        return firmware_model_id.get(type_id, "Controller")
