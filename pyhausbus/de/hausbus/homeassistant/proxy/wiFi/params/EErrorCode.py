import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ERROR=0
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



