import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.counter.params.MMode import MMode
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
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param mode increment: 1 = Zaehler inkrementieren.
  @param debounceTime 0 - 255[ms].
  @param reportTime Zeitintervall in Minuten nach dem der Zaehler den aktuellen Stand meldet.
  @param scaleFaktor Anzahl Impulse pro Einheit z.B. pro kWh.
  """
  def setConfiguration(self, mode:MMode, debounceTime:int, reportTime:int, scaleFaktor:int):
    logging.info("setConfiguration"+" mode = "+str(mode)+" debounceTime = "+str(debounceTime)+" reportTime = "+str(reportTime)+" scaleFaktor = "+str(scaleFaktor))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(mode.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.addWord(reportTime)
    hbCommand.addWord(scaleFaktor)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 2, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def setCount(self, counter:int, fraction:int):
    logging.info("setCount"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 3, "setCount")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    hbCommand.send()
    logging.info("returns")

  """
  @param mode increment: 1 = Zaehler inkrementieren.
  @param debounceTime 0 - 255[ms].
  @param reportTime Zeitintervall in Minuten nach dem der Zaehler den aktuellen Stand meldet.
  @param scaleFaktor Anzahl Impulse pro Einheit z.B. pro kWh.
  """
  def Configuration(self, mode:MMode, debounceTime:int, reportTime:int, scaleFaktor:int):
    logging.info("Configuration"+" mode = "+str(mode)+" debounceTime = "+str(debounceTime)+" reportTime = "+str(reportTime)+" scaleFaktor = "+str(scaleFaktor))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(mode.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.addWord(reportTime)
    hbCommand.addWord(scaleFaktor)
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def Status(self, counter:int, fraction:int):
    logging.info("Status"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    hbCommand.send()
    logging.info("returns")

  """
  @param counter Zaehler ganze Einheiten.
  @param fraction Bruchteil 0-scaleFactor.
  """
  def evStatus(self, counter:int, fraction:int):
    logging.info("evStatus"+" counter = "+str(counter)+" fraction = "+str(fraction))
    hbCommand = HausBusCommand(self.objectId, 200, "evStatus")
    hbCommand.addDWord(counter)
    hbCommand.addWord(fraction)
    hbCommand.send()
    logging.info("returns")


