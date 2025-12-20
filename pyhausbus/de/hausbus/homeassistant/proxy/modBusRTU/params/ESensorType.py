import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ESensorType(Enum):
  eUnknown=0
  eTemperature=1
  eHumidity=2
  eDewPoint=3
  eDistance=4
  eBrightness=5
  ePower=6
  eCounter=7
  eAnalogInput=8
  eModBusRegister=9
  eCO2=10
  eTVOC=11
  ePressure=12
  eVoltage=13
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ESensorType.__members__.values():
      if (act.value == checkValue):
        return act

    return ESensorType.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ESensorType':
    try:
      return ESensorType[name]
    except KeyError:
      return ESensorType.SER_UNKNOWN 




