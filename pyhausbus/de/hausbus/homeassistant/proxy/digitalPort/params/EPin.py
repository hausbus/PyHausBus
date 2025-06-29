import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EPin(Enum):
  UNUSED=255
  TASTER=16
  SCHALTER=19
  LED=21
  OW_BUS=32
  IR_SENSOR=33
  DHT_SENSOR=34
  COUNTER=35
  ROLLO_HOCH_4=128
  ROLLO_RUNTER_4=129
  S0_READER=40
  RFID_D0=43
  RFID_D1=130
  ANALOG_IN=36
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EPin.__members__.values():
      if (act.value == checkValue):
        return act

    return EPin.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EPin':
    try:
      return EPin[name]
    except KeyError:
      return EPin.SER_UNKNOWN 




