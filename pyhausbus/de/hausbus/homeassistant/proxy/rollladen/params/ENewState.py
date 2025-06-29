import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class ENewState(Enum):
  NO_COMMAND=0
  START_MOTOR=1
  MOTOR_IS_RUNNING=2
  STOP_MOTOR=3
  NOTIFY_RUNNING=4
  NOTIFY_STOPPED=5
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ENewState.__members__.values():
      if (act.value == checkValue):
        return act

    return ENewState.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'ENewState':
    try:
      return ENewState[name]
    except KeyError:
      return ENewState.SER_UNKNOWN 




