import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.params.ELastEvent import ELastEvent

class PowerMeter(ABusFeature):
  CLASS_ID:int = 41

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return PowerMeter(HausBusUtils.getObjectId(deviceId, 41, instanceId))

  """
  """
  def evLowPower(self):
    logging.info("evLowPower")
    hbCommand = HausBusCommand(self.objectId, 200, "evLowPower")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evMediumPower(self):
    logging.info("evMediumPower")
    hbCommand = HausBusCommand(self.objectId, 201, "evMediumPower")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evHighPower(self):
    logging.info("evHighPower")
    hbCommand = HausBusCommand(self.objectId, 202, "evHighPower")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param lowerThreshold untere Leistungsschwelle[kWh].
  @param lowerThresholdFraction Nachkommastellen der unteren Leistungsschwelle[00-99].
  @param upperThreshold obere Leistungsschwelle[kWh].
  @param upperThresholdFraction Nachkommastellen der oberen Leistungsschwelle[00-99].
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Prozent].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def setConfiguration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("setConfiguration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addSByte(lowerThreshold)
    hbCommand.addSByte(lowerThresholdFraction)
    hbCommand.addSByte(upperThreshold)
    hbCommand.addSByte(upperThresholdFraction)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 2, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param lowerThreshold untere Leistungsschwelle[kWh].
  @param lowerThresholdFraction Nachkommastellen der unteren Leistungsschwelle[00-99].
  @param upperThreshold obere Leistungsschwelle[kWh].
  @param upperThresholdFraction Nachkommastellen der oberen Leistungsschwelle[00-99].
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Prozent].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def Configuration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("Configuration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addSByte(lowerThreshold)
    hbCommand.addSByte(lowerThresholdFraction)
    hbCommand.addSByte(upperThreshold)
    hbCommand.addSByte(upperThresholdFraction)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param power Aktueller Stromverbrauch.
  @param centiPower hundertstel Stromverbrauch.
  @param lastEvent .
  """
  def Status(self, power:int, centiPower:int, lastEvent:ELastEvent):
    logging.info("Status"+" power = "+str(power)+" centiPower = "+str(centiPower)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addSByte(power)
    hbCommand.addSByte(centiPower)
    hbCommand.addByte(lastEvent.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param power Stromverbrauch [kWh].
  @param centiPower hundertstel Stromverbrauch.
  @param lastEvent .
  """
  def evStatus(self, power:int, centiPower:int, lastEvent:ELastEvent):
    logging.info("evStatus"+" power = "+str(power)+" centiPower = "+str(centiPower)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 203, "evStatus")
    hbCommand.addSByte(power)
    hbCommand.addSByte(centiPower)
    hbCommand.addByte(lastEvent.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")


