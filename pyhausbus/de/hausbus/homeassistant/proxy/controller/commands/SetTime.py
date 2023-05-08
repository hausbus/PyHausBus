from pyhausbus.WeekTime import WeekTime
import pyhausbus.HausBusUtils as HausBusUtils

class SetTime:
  CLASS_ID = 0
  FUNCTION_ID = 125

  def __init__(self,weekTime:WeekTime):
    self.weekTime=weekTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetTime(WeekTime._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetTime(weekTime={self.weekTime})"

  '''
  @param weekTime .
  '''
  def getWeekTime(self):
    return self.weekTime



