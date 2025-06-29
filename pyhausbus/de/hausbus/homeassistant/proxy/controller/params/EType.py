import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EType(Enum):
  BIT=0
  BYTE=1
  WORD=2
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EType.__members__.values():
      if (act.value == checkValue):
        return act

    return EType.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EType':
    try:
      return EType[name]
    except KeyError:
      return EType.SER_UNKNOWN 




