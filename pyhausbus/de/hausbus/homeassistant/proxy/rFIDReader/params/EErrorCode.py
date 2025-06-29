import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  OK=0
  NO_DATA=1
  DATA_OVERFLOW=2
  INVALID_BIT_COUNT=3
  DATA_CORRUPT=4
  DISCONNECTED=16
  NOT_CONNECTED=17
  ANY_ERROR=255
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EErrorCode':
    try:
      return EErrorCode[name]
    except KeyError:
      return EErrorCode.SER_UNKNOWN 




