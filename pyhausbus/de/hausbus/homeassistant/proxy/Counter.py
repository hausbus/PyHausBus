from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.counter.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.counter.params.MMode import MMode
from pyhausbus.de.hausbus.homeassistant.proxy.counter.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.counter.params.EErrorCode import EErrorCode

class Counter(ABusFeature):
  CLASS_ID:int = 35

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Counter(HausBusUtils.getObjectId(deviceId, 35, instanceId))

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param mode increment: 1 = Zaehler inkrementieren.
  @param debounceTime 0 - 255[ms].
  @param reportTime Zeitintervall in Minuten nach dem der Zaehler den aktuellen Stand meldet.
  @param scaleFaktor Anzahl Impulse pro Einheit z.B. pro kWh.
  """
  def setConfiguration(self, mode:MMode, debounceTime:int, reportTime:int, scaleFaktor:int):
    LOGGER.debug("setConfiguration"+" mode = "+str(mode)+" debounceTime = "+str(debounceTime)+" reportTime = "+str(reportTime)+" scaleFaktor = "+str(scaleFaktor))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(mode.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.addWord(reportTime)
    hbCommand.addWord(scaleFaktor)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getStatus(self):
    LOGGER.debug("getStatus")
    hbCommand = HausBusCommand(self.objectId, 2, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def setCount(self, counter:int, fraction:int):
    LOGGER.debug("setCount"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 3, "setCount")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param mode increment: 1 = Zaehler inkrementieren.
  @param debounceTime 0 - 255[ms].
  @param reportTime Zeitintervall in Minuten nach dem der Zaehler den aktuellen Stand meldet.
  @param scaleFaktor Anzahl Impulse pro Einheit z.B. pro kWh.
  """
  def Configuration(self, mode:MMode, debounceTime:int, reportTime:int, scaleFaktor:int):
    LOGGER.debug("Configuration"+" mode = "+str(mode)+" debounceTime = "+str(debounceTime)+" reportTime = "+str(reportTime)+" scaleFaktor = "+str(scaleFaktor))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(mode.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.addWord(reportTime)
    hbCommand.addWord(scaleFaktor)
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

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def Status(self, counter:int, fraction:int):
    LOGGER.debug("Status"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def evStatus(self, counter:int, fraction:int):
    LOGGER.debug("evStatus"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 200, "evStatus")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


