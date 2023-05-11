import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EFeatureId(Enum):
  RFID=0
  PID=1
  MOD_BUS=2
  WIFI=3
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EFeatureId.__members__.values():
      if (act.value == checkValue):
        return act

    return EFeatureId.SER_UNKNOWN



