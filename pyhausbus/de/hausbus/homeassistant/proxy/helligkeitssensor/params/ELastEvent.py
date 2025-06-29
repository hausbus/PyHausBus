import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ELastEvent(Enum):
  DARK=200
  LIGHT=201
  BRIGHT=202
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ELastEvent.__members__.values():
      if (act.value == checkValue):
        return act

    return ELastEvent.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ELastEvent':
    try:
      return ELastEvent[name]
    except KeyError:
      return ELastEvent.SER_UNKNOWN 




