import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  ANY_ERROR=255
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EFirmwareId':
    try:
      return EFirmwareId[name]
    except KeyError:
      return EFirmwareId.SER_UNKNOWN 




