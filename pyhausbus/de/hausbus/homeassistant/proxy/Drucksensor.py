from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.params.ELastEvent import ELastEvent
from pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.Status import Status

class Drucksensor(ABusFeature):
  CLASS_ID:int = 48

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Drucksensor(HausBusUtils.getObjectId(deviceId, 48, instanceId))

  """
  """
  def evLow(self):
    LOGGER.debug("evLow")
    hbCommand = HausBusCommand(self.objectId, 200, "evLow")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evInRange(self):
    LOGGER.debug("evInRange")
    hbCommand = HausBusCommand(self.objectId, 201, "evInRange")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evHigh(self):
    LOGGER.debug("evHigh")
    hbCommand = HausBusCommand(self.objectId, 202, "evHigh")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param value gemessener Druck in Pa.
  @param lastEvent .
  """
  def evStatus(self, value:int, lastEvent:ELastEvent):
    LOGGER.debug("evStatus"+" value = "+str(value)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 203, "evStatus")
    hbCommand.addWord(value)
    hbCommand.addByte(lastEvent.value)
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
  @param lowerThreshold untere Schwelle.
  @param upperThreshold obere Schwelle.
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime [s].
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren..
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def setConfiguration(self, lowerThreshold:int, upperThreshold:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    LOGGER.debug("setConfiguration"+" lowerThreshold = "+str(lowerThreshold)+" upperThreshold = "+str(upperThreshold)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addWord(lowerThreshold)
    hbCommand.addWord(upperThreshold)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
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
  @param lowerThreshold untere Schwelle.
  @param upperThreshold obere Schwelle.
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime [s].
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren..
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def Configuration(self, lowerThreshold:int, upperThreshold:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    LOGGER.debug("Configuration"+" lowerThreshold = "+str(lowerThreshold)+" upperThreshold = "+str(upperThreshold)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addWord(lowerThreshold)
    hbCommand.addWord(upperThreshold)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addByte(calibration)
    hbCommand.addByte(deltaSensorID)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param value aktuell gemessener Druck in Pa.
  @param lastEvent .
  """
  def Status(self, value:int, lastEvent:ELastEvent):
    LOGGER.debug("Status"+" value = "+str(value)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addWord(value)
    hbCommand.addByte(lastEvent.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


