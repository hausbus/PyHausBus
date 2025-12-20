import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ERegisterType(Enum):
  NONE=0
  eSignedWordHolding=2
  eSignedWordInput=3
  eUnsignedWordHolding=4
  eUnsignedWordInput=5
  eSignedDWordHolding=6
  eSignedDWordInput=7
  eUnsignedDWordHolding=8
  eUnsignedDWordInput=9
  eFloatHolding=10
  eFloatInput=11
  eVoltage=12
  eCurrent=13
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ERegisterType.__members__.values():
      if (act.value == checkValue):
        return act

    return ERegisterType.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ERegisterType':
    try:
      return ERegisterType[name]
    except KeyError:
      return ERegisterType.SER_UNKNOWN 




