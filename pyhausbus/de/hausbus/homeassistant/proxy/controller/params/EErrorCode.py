import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ERROR=0
  MODULE_NOT_EXISTS=1
  MEMORY_WRITE_FAILED=2
  INVALID_RULE_TABLE=3
  SYNTAX_ERROR=4
  NULL_POINTER=5
  LOW_VOLTAGE=6
  WATCHDOG=7
  INVALID_FW_LOADED=8
  MSG_QUEUE_OVERRUN=9
  CHECKSUM_ERROR=16
  CHECKSUM_ERROR_CONF_FLASH=17
  CHECKSUM_ERROR_CONF_EEPROM=18
  UNIT_GROUP_NOT_EXISTS=19
  MAX_OBJECTS_REACHED=10
  MODBUS_STREAM_NOT_EXISTS=20
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



