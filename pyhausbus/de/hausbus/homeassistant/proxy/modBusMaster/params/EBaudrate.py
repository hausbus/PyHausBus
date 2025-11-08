import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EBaudrate(Enum):
  _1200=0
  _2400=1
  _4800=2
  _9600=3
  _19200=4
  _38400=5
  _57600=6
  _115200=7
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EBaudrate.__members__.values():
      if (act.value == checkValue):
        return act

    return EBaudrate.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EBaudrate':
    try:
      return EBaudrate[name]
    except KeyError:
      return EBaudrate.SER_UNKNOWN 




