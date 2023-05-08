from pyhausbus.WeekTime import WeekTime
import pyhausbus.HausBusUtils as HausBusUtils

class EvTime:
  CLASS_ID = 0
  FUNCTION_ID = 200

  def __init__(self,weektime:WeekTime):
    self.weektime=weektime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvTime(WeekTime._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvTime(weektime={self.weektime})"

  '''
  @param weektime .
  '''
  def getWeektime(self):
    return self.weektime



