import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ESlotType(Enum):
  UNUSED=0
  DIMMER=1
  SOCKET=2
  SHUTTER=3
  DOUBLE_SWITCH=7
  SOFT_START_SWITCH=8
  DIMMER_V30=10
  DIMMER_V31=11
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ESlotType.__members__.values():
      if (act.value == checkValue):
        return act

    return ESlotType.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ESlotType':
    try:
      return ESlotType[name]
    except KeyError:
      return ESlotType.SER_UNKNOWN 




