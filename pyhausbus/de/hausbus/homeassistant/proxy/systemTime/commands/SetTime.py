from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EWeekDay import EWeekDay
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EDate import EDate
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EMonth import EMonth
import pyhausbus.HausBusUtils as HausBusUtils

class SetTime:
  CLASS_ID = 3
  FUNCTION_ID = 1

  def __init__(self,weekDay:EWeekDay, date:EDate, month:EMonth, year:int, hours:int, minutes:int, seconds:int):
    self.weekDay=weekDay
    self.date=date
    self.month=month
    self.year=year
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetTime(EWeekDay._fromBytes(dataIn, offset), EDate._fromBytes(dataIn, offset), EMonth._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetTime(weekDay={self.weekDay}, date={self.date}, month={self.month}, year={self.year}, hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

  '''
  @param weekDay .
  '''
  def getWeekDay(self):
    return self.weekDay

  '''
  @param date .
  '''
  def getDate(self):
    return self.date

  '''
  @param month .
  '''
  def getMonth(self):
    return self.month

  '''
  @param year .
  '''
  def getYear(self):
    return self.year

  '''
  @param hours .
  '''
  def getHours(self):
    return self.hours

  '''
  @param minutes .
  '''
  def getMinutes(self):
    return self.minutes

  '''
  @param seconds .
  '''
  def getSeconds(self):
    return self.seconds



