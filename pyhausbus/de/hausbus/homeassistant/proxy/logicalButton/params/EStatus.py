import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EStatus(Enum):
  OFF=0
  ON=1
  BLINK=2
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EStatus.__members__.values():
      if (act.value == checkValue):
        return act

    return EStatus.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EStatus':
    try:
      return EStatus[name]
    except KeyError:
      return EStatus.SER_UNKNOWN 




