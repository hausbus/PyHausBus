import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  CMD_NOT_SUPPORTED=130
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



