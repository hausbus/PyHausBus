import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EValue(Enum):
  DISABLE=0
  ENABLE=1
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EValue.__members__.values():
      if (act.value == checkValue):
        return act

    return EValue.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EValue':
    try:
      return EValue[name]
    except KeyError:
      return EValue.SER_UNKNOWN 




