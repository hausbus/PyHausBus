import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EState(Enum):
  ANY=255
  RELEASED=0
  PRESSED=1
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EState.__members__.values():
      if (act.value == checkValue):
        return act

    return EState.SER_UNKNOWN



