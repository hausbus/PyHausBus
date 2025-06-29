import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ERROR=0
  TIMEOUT=1
  NOT_SUPPORTED_SENSOR_OBJECT=2
  NOT_SUPPORTED_ACTOR_OBJECT=3
  MAX_INSTANCES_REACHED=4
  CONFIGURATION_OUT_OF_MEMORY=128
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
  def value_of(name: str) -> 'EErrorCode':
    try:
      return EErrorCode[name]
    except KeyError:
      return EErrorCode.SER_UNKNOWN 




