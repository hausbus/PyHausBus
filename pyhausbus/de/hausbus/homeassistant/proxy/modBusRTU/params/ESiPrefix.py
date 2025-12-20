import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ESiPrefix(Enum):
  eMicro=-6
  eMilli=-3
  eCenti=-2
  eDeci=-1
  eBase=0
  eDeka=1
  eHecto=2
  eKilo=3
  eMega=6
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ESiPrefix.__members__.values():
      if (act.value == checkValue):
        return act

    return ESiPrefix.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ESiPrefix':
    try:
      return ESiPrefix[name]
    except KeyError:
      return ESiPrefix.SER_UNKNOWN 




