from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EMode import EMode
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EDirection import EDirection
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EErrorCode import EErrorCode

class Dimmer(ABusFeature):
  CLASS_ID:int = 17

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Dimmer(HausBusUtils.getObjectId(deviceId, 17, instanceId))

  """
  @param brightness aktuelle Helligkeit 0-100%.
  @param duration Einschaltdauer: Wert in Sekunden\r\n0=Endlos.
  """
  def evOn(self, brightness:int, duration:int):
    LOGGER.debug("evOn"+" brightness = "+str(brightness)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param mode DIMM_CR: dieser Mode ist zu Verwenden.
  @param fadingTime Zeit a 50ms um 0-100% zu dimmen.
  @param dimmingTime Zeit a 50ms um 0-100% zu dimmen.
  @param dimmingRangeStart Startwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  @param dimmingRangeEnd Endwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  """
  def setConfiguration(self, mode:EMode, fadingTime:int, dimmingTime:int, dimmingRangeStart:int, dimmingRangeEnd:int):
    LOGGER.debug("setConfiguration"+" mode = "+str(mode)+" fadingTime = "+str(fadingTime)+" dimmingTime = "+str(dimmingTime)+" dimmingRangeStart = "+str(dimmingRangeStart)+" dimmingRangeEnd = "+str(dimmingRangeEnd))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(mode.value)
    hbCommand.addByte(fadingTime)
    hbCommand.addByte(dimmingTime)
    hbCommand.addByte(dimmingRangeStart)
    hbCommand.addByte(dimmingRangeEnd)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param brightness Helligkeit in Prozent.
  @param duration Einschaltdauer in Sekunden.
  """
  def setBrightness(self, brightness:int, duration:int):
    LOGGER.debug("setBrightness"+" brightness = "+str(brightness)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 2, "setBrightness")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param mode DIMM_CR: Dimmer arbeitet mit Phasenabschnitt\r\nDIMM_L: Dimmer arbeitet mit Phasenanschnitt\r\nSWITCH: Dimmer schaltet nur keine Dimmfunktion\r\n\r\nACHTUNG: EIN FALSCHER MODE.
  @param fadingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu schalten.
  @param dimmingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu dimmen.
  @param dimmingRangeStart Startwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  @param dimmingRangeEnd Endwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  """
  def Configuration(self, mode:EMode, fadingTime:int, dimmingTime:int, dimmingRangeStart:int, dimmingRangeEnd:int):
    LOGGER.debug("Configuration"+" mode = "+str(mode)+" fadingTime = "+str(fadingTime)+" dimmingTime = "+str(dimmingTime)+" dimmingRangeStart = "+str(dimmingRangeStart)+" dimmingRangeEnd = "+str(dimmingRangeEnd))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(mode.value)
    hbCommand.addByte(fadingTime)
    hbCommand.addByte(dimmingTime)
    hbCommand.addByte(dimmingRangeStart)
    hbCommand.addByte(dimmingRangeEnd)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOff(self):
    LOGGER.debug("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param direction .
  """
  def evStart(self, direction:EDirection):
    LOGGER.debug("evStart"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 202, "evStart")
    hbCommand.addByte(direction.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param direction .
  """
  def start(self, direction:EDirection):
    LOGGER.debug("start"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 3, "start")
    hbCommand.addByte(direction.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def stop(self):
    LOGGER.debug("stop")
    hbCommand = HausBusCommand(self.objectId, 4, "stop")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getStatus(self):
    LOGGER.debug("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param brightness aktuelle Helligkeit 0-100%.
  @param duration Einschaltdauer: Wert in Sekunden\r\n0=Endlos.
  """
  def Status(self, brightness:int, duration:int):
    LOGGER.debug("Status"+" brightness = "+str(brightness)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode NO_ZERO_CROSS_DETECTED: Nulldurchgaenge koennen nicht detektiert werde.
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


