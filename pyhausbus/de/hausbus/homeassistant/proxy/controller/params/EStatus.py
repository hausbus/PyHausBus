import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EStatus(Enum):
  OK=0
  LOCKED=1
  ABORTED=2
  STOPPED=3
  RESET=4
  INVALID_BUFFER=5
  INVALID=255
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




