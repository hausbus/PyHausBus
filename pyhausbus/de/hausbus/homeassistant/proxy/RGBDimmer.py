import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *

class RGBDimmer(ABusFeature):
  CLASS_ID:int = 22

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  """
  def evOff(self):
    logging.info("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    hbCommand.send()
    logging.info("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def evOn(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    logging.info("evOn"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
    hbCommand.send()
    logging.info("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def setColor(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    logging.info("setColor"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 2, "setColor")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
    hbCommand.send()
    logging.info("returns")

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
  @param fadingTime Zeit a 50ms um 0-100% zu dimmen.
  """
  def setConfiguration(self, fadingTime:int):
    logging.info("setConfiguration"+" fadingTime = "+str(fadingTime))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(fadingTime)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param fadingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu schalten.
  """
  def Configuration(self, fadingTime:int):
    logging.info("Configuration"+" fadingTime = "+str(fadingTime))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(fadingTime)
    hbCommand.send()
    logging.info("returns")

  """
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  @param duration Einschaltdauer in Sekunden.
  """
  def Status(self, brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    logging.info("Status"+" brightnessRed = "+str(brightnessRed)+" brightnessGreen = "+str(brightnessGreen)+" brightnessBlue = "+str(brightnessBlue)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(brightnessRed)
    hbCommand.addByte(brightnessGreen)
    hbCommand.addByte(brightnessBlue)
    hbCommand.addWord(duration)
    hbCommand.send()
    logging.info("returns")


