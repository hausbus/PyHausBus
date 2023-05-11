import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  OK=0
  START_FAIL=1
  FAILTURE=2
  CRC_FAILTURE=3
  OUT_OF_MEMORY=4
  BUS_HUNG=5
  NOT_PRESENT=6
  ACK_TOO_LONG=7
  SYNC_TIMEOUT=8
  DATA_TIMEOUT=9
  CHECKSUM_ERROR=10
  ACK_MISSING=11
  RESULT_NOT_AVAILABLE=12
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



