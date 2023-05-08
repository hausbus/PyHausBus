import pyhausbus.HausBusUtils as HausBusUtils

class Time:
  CLASS_ID = 3
  FUNCTION_ID = 128

  def __init__(self,weekday:int, date:int, month:int, year:int, hours:int, minutes:int, seconds:int):
    self.weekday=weekday
    self.date=date
    self.month=month
    self.year=year
    self.hours=hours
    self.minutes=minutes
    self.seconds=seconds


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Time(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Time(weekday={self.weekday}, date={self.date}, month={self.month}, year={self.year}, hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

  '''
  @param weekday .
  '''
  def getWeekday(self):
    return self.weekday

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



