import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EReason(Enum):
  PowerOn=1
  External=2
  BrownOut=4
  Watchdog=8
  Debug=16
  Software=32
  Unknown=0
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EReason.__members__.values():
      if (act.value == checkValue):
        return act

    return EReason.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EReason':
    try:
      return EReason[name]
    except KeyError:
      return EReason.SER_UNKNOWN 




