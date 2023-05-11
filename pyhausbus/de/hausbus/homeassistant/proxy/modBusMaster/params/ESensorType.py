import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ESensorType(Enum):
  NONE=0
  SDM_TOTAL_POWER=1
  SDM_IMPORT_POWER=2
  SDM_EXPORT_POWER=3
  SDM_IMPORT_ENERGY=4
  SDM_EXPORT_ENERGY=5
  ORWE517_TOTAL_POWER=6
  ORWE517_TOTAL_ENERGY=7
  ORWE517_FORWARD_ENERGY=8
  ORWE517_REVERSE_ENERGY=9
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ESensorType.__members__.values():
      if (act.value == checkValue):
        return act

    return ESensorType.SER_UNKNOWN



