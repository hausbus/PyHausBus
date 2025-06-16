import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EEnable(Enum):
  OFF=0
  ON=1
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EEnable.__members__.values():
      if (act.value == checkValue):
        return act

    return EEnable.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EFirmwareId':
    try:
      return EFirmwareId[name]
    except KeyError:
      return EFirmwareId.SER_UNKNOWN 




