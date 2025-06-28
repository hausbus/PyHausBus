from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.data.Time import Time
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EWeekDay import EWeekDay
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EDate import EDate
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EMonth import EMonth
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EErrorCode import EErrorCode

class SystemTime(ABusFeature):
  CLASS_ID:int = 3

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return SystemTime(HausBusUtils.getObjectId(deviceId, 3, instanceId))

  """
  """
  def getTime(self):
    LOGGER.debug("getTime")
    hbCommand = HausBusCommand(self.objectId, 0, "getTime")
    ResultWorker()._setResultInfo(Time,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param weekDay .
  @param date .
  @param month .
  @param year .
  @param hours .
  @param minutes .
  @param seconds .
  """
  def setTime(self, weekDay:EWeekDay, date:EDate, month:EMonth, year:int, hours:int, minutes:int, seconds:int):
    LOGGER.debug("setTime"+" weekDay = "+str(weekDay)+" date = "+str(date)+" month = "+str(month)+" year = "+str(year)+" hours = "+str(hours)+" minutes = "+str(minutes)+" seconds = "+str(seconds))
    hbCommand = HausBusCommand(self.objectId, 1, "setTime")
    hbCommand.addByte(weekDay.value)
    hbCommand.addByte(date.value)
    hbCommand.addByte(month.value)
    hbCommand.addWord(year)
    hbCommand.addByte(hours)
    hbCommand.addByte(minutes)
    hbCommand.addByte(seconds)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param weekday .
  @param date .
  @param month .
  @param year .
  @param hours .
  @param minutes .
  @param seconds .
  """
  def Time(self, weekday:int, date:int, month:int, year:int, hours:int, minutes:int, seconds:int):
    LOGGER.debug("Time"+" weekday = "+str(weekday)+" date = "+str(date)+" month = "+str(month)+" year = "+str(year)+" hours = "+str(hours)+" minutes = "+str(minutes)+" seconds = "+str(seconds))
    hbCommand = HausBusCommand(self.objectId, 128, "Time")
    hbCommand.addByte(weekday)
    hbCommand.addByte(date)
    hbCommand.addByte(month)
    hbCommand.addWord(year)
    hbCommand.addByte(hours)
    hbCommand.addByte(minutes)
    hbCommand.addByte(seconds)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


