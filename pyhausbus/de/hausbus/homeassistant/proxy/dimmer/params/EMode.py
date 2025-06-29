import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EMode(Enum):
  DIMM_CR=0
  DIMM_L=1
  SWITCH=2
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EMode.__members__.values():
      if (act.value == checkValue):
        return act

    return EMode.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EMode':
    try:
      return EMode[name]
    except KeyError:
      return EMode.SER_UNKNOWN 




