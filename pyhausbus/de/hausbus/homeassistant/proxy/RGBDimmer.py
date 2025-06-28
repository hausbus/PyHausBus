from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.Status import Status

class RGBDimmer(ABusFeature):
  CLASS_ID:int = 22

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return RGBDimmer(HausBusUtils.getObjectId(deviceId, 22, instanceId))

  """
  """
  def evOff(self):
    LOGGER.debug("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def evOn(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    LOGGER.debug("evOn"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def setColor(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    LOGGER.debug("setColor"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 2, "setColor")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
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
  @param fadingTime Zeit a 50ms um 0-100% zu dimmen.
  """
  def setConfiguration(self, fadingTime:int):
    LOGGER.debug("setConfiguration"+" fadingTime = "+str(fadingTime))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(fadingTime)
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
  @param fadingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu schalten.
  """
  def Configuration(self, fadingTime:int):
    LOGGER.debug("Configuration"+" fadingTime = "+str(fadingTime))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(fadingTime)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def Status(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    LOGGER.debug("Status"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


