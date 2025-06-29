import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EState(Enum):
  STARTUP=0
  STANDBY=1
  IDLE=2
  CONNECTED=3
  DISCONNECTED=4
  UNKNOWN=255
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EState.__members__.values():
      if (act.value == checkValue):
        return act

    return EState.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EState':
    try:
      return EState[name]
    except KeyError:
      return EState.SER_UNKNOWN 




