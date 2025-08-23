import pyhausbus.HausBusUtils as HausBusUtils

class WeekTime:

  def __init__(self, day:int, hour:int, minute:int):
    self.day = day
    self.hour = hour
    self.minute = minute

  @staticmethod
  def _fromBytes(data: bytearray, offset: int) -> 'WeekTime':
    value = HausBusUtils.bytesToWord(data, offset)

    minute = value & 0xff
    value = value >> 8
    hour = value & 0x1F
    day = value >> 5
    return WeekTime(day, hour, minute)

  def getValue(self) -> int:
    value = self.day << 5
    value += self.hour
    value = value << 8
    value += self.minute
    return value

  @staticmethod
  def _fromValue(value:int) -> 'WeekTime':
    result = WeekTime(0,0,0)
    result.setMinute(value & 0xff)

    value = value >> 8
    result.setHour(value & 0x1F)
    result.setDay(value >> 5)
    return result

  def getDay(self) -> int:
    return self.day

  def setDay(self, day:int):
    self.day = day

  def getHour(self) -> int:
    return self.hour

  def setHour(self, hour:int):
    self.hour = hour

  def getMinute(self) -> int:
    return self.minute

  def setMinute(self, minute:int):
    self.minute = minute

  def __str__(self):
    return f"WeekTime(day={self.day}, hour={self.hour}, minute={self.minute})"