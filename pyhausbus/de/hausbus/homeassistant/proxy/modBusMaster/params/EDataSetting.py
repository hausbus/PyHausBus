import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EDataSetting(Enum):
  8N1=128
  8E1=132
  8O1=136
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EDataSetting.__members__.values():
      if (act.value == checkValue):
        return act

    return EDataSetting.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EDataSetting':
    try:
      return EDataSetting[name]
    except KeyError:
      return EDataSetting.SER_UNKNOWN 




