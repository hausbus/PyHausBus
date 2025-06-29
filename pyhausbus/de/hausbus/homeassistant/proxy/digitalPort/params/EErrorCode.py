import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  PIN0_FUNCTION_NOT_SUPPORTED=16
  PIN1_FUNCTION_NOT_SUPPORTED=17
  PIN2_FUNCTION_NOT_SUPPORTED=18
  PIN3_FUNCTION_NOT_SUPPORTED=19
  PIN4_FUNCTION_NOT_SUPPORTED=20
  PIN5_FUNCTION_NOT_SUPPORTED=21
  PIN6_FUNCTION_NOT_SUPPORTED=22
  PIN7_FUNCTION_NOT_SUPPORTED=23
  PIN0_FUNCTION_NOT_ACTIVATED=24
  PIN1_FUNCTION_NOT_ACTIVATED=25
  PIN2_FUNCTION_NOT_ACTIVATED=26
  PIN3_FUNCTION_NOT_ACTIVATED=27
  PIN4_FUNCTION_NOT_ACTIVATED=28
  PIN5_FUNCTION_NOT_ACTIVATED=29
  PIN6_FUNCTION_NOT_ACTIVATED=30
  PIN7_FUNCTION_NOT_ACTIVATED=31
  CONFIGURATION_OUT_OF_MEMORY=128
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




