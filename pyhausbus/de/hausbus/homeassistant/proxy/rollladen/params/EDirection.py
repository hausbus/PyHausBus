import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EDirection(Enum):
  ANY=255
  TOGGLE=0
  TO_CLOSE=1
  TO_OPEN=2
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EDirection.__members__.values():
      if (act.value == checkValue):
        return act

    return EDirection.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EDirection':
    try:
      return EDirection[name]
    except KeyError:
      return EDirection.SER_UNKNOWN 




