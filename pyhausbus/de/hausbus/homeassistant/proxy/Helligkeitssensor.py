import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.params.ELastEvent import ELastEvent
from pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.params.EErrorCode import EErrorCode

class Helligkeitssensor(ABusFeature):
  CLASS_ID:int = 39

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Helligkeitssensor(HausBusUtils.getObjectId(deviceId, 39, instanceId))

  """
  @param brightness Helligkeitswert.
  @param lastEvent .
  """
  def evStatus(self, brightness:int, lastEvent:ELastEvent):
    logging.info("evStatus"+" brightness = "+str(brightness)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 203, "evStatus")
    hbCommand.addWord(brightness)
    hbCommand.addByte(lastEvent.value)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evDark(self):
    logging.info("evDark")
    hbCommand = HausBusCommand(self.objectId, 200, "evDark")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evLight(self):
    logging.info("evLight")
    hbCommand = HausBusCommand(self.objectId, 201, "evLight")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evBright(self):
    logging.info("evBright")
    hbCommand = HausBusCommand(self.objectId, 202, "evBright")
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
  @param lowerThreshold untere Helligkeitsschwelle.
  @param upperThreshold obere Helligkeitsschwelle.
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [10 lux].
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [10 lux].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def setConfiguration(self, lowerThreshold:int, upperThreshold:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("setConfiguration"+" lowerThreshold = "+str(lowerThreshold)+" upperThreshold = "+str(upperThreshold)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addWord(lowerThreshold)
    hbCommand.addWord(upperThreshold)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
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
  @param lowerThreshold untere Helligkeitsschwelle.
  @param upperThreshold obere Helligkeitsschwelle.
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [10 lux].
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [10 lux].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def Configuration(self, lowerThreshold:int, upperThreshold:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("Configuration"+" lowerThreshold = "+str(lowerThreshold)+" upperThreshold = "+str(upperThreshold)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addWord(lowerThreshold)
    hbCommand.addWord(upperThreshold)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
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
  @param brightness Helligkeitswert.
  @param lastEvent .
  """
  def Status(self, brightness:int, lastEvent:ELastEvent):
    logging.info("Status"+" brightness = "+str(brightness)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addWord(brightness)
    hbCommand.addByte(lastEvent.value)
    hbCommand.send()
    logging.info("returns")


