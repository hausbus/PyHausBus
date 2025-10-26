import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EFunction(Enum):
  READ_COILS=1
  READ_DISCRETE_INPUTS=2
  READ_HOLDING_REGISTERS=3
  READ_INPUT_REGISTERS=4
  WRITE_SINGLE_COIL=5
  WRITE_SINGLE_REGISTER=6
  WRITE_MULTIPLE_COILS=15
  WRITE_MULTIPLE_REGISTERS=16
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EFunction.__members__.values():
      if (act.value == checkValue):
        return act

    return EFunction.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EFunction':
    try:
      return EFunction[name]
    except KeyError:
      return EFunction.SER_UNKNOWN 




