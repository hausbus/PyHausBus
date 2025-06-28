from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.WeekTime import WeekTime

class Wetter(ABusFeature):
  CLASS_ID:int = 2

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Wetter(HausBusUtils.getObjectId(deviceId, 2, instanceId))

  """
  """
  def getWeather(self):
    LOGGER.debug("getWeather")
    hbCommand = HausBusCommand(self.objectId, 5, "getWeather")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param humidity Luftfeuchtigkeit.
  @param pressure Luftdruck.
  @param temp Temperatur.
  @param sunrise Zeitpunkt vom Sonnenaufgang.
  @param sunset Zeitpunkt vom Sonnenuntergang.
  @param text Beschreibung.
  """
  def weather(self, humidity:int, pressure:int, temp:int, sunrise:WeekTime=None
, sunset:WeekTime=None
, text:str):
    LOGGER.debug("weather"+" humidity = "+str(humidity)+" pressure = "+str(pressure)+" temp = "+str(temp)+" sunrise = "+str(sunrise)+" sunset = "+str(sunset)+" text = "+str(text))
    hbCommand = HausBusCommand(self.objectId, 128, "weather")
    hbCommand.addByte(humidity)
    hbCommand.addWord(pressure)
    hbCommand.addByte(temp)
    hbCommand.addWord(sunrise.getValue())
    hbCommand.addWord(sunset.getValue())
    hbCommand.addString(text)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


