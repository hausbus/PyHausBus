import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ERROR=0
  TWI_BUSY=1
  TWI_READ_FAILED=2
  TWI_WRITE_FAILED=3
  CLOCK_HALTED=4
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



