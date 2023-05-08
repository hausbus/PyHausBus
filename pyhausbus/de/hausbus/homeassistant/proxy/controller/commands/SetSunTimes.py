from pyhausbus.WeekTime import WeekTime
import pyhausbus.HausBusUtils as HausBusUtils

class SetSunTimes:
  CLASS_ID = 0
  FUNCTION_ID = 15

  def __init__(self,sunriseTime:WeekTime, sunsetTime:WeekTime):
    self.sunriseTime=sunriseTime
    self.sunsetTime=sunsetTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetSunTimes(WeekTime._fromBytes(dataIn, offset), WeekTime._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetSunTimes(sunriseTime={self.sunriseTime}, sunsetTime={self.sunsetTime})"

  '''
  @param sunriseTime Zeit fuer den Sonnenaufgang..
  '''
  def getSunriseTime(self):
    return self.sunriseTime

  '''
  @param sunsetTime Zeit fuer den Sonnenuntergang..
  '''
  def getSunsetTime(self):
    return self.sunsetTime



