import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EMonth(Enum):
  January=1
  February=2
  March=3
  April=4
  May=5
  June=6
  July=7
  August=8
  September=9
  October=10
  November=11
  December=12
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EMonth.__members__.values():
      if (act.value == checkValue):
        return act

    return EMonth.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EMonth':
    try:
      return EMonth[name]
    except KeyError:
      return EMonth.SER_UNKNOWN 




