import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EWeekDay(Enum):
  Monday=1
  Tuesday=2
  Wednesday=3
  Thursday=4
  Friday=5
  Saturday=6
  Sunday=7
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EWeekDay.__members__.values():
      if (act.value == checkValue):
        return act

    return EWeekDay.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EWeekDay':
    try:
      return EWeekDay[name]
    except KeyError:
      return EWeekDay.SER_UNKNOWN 




