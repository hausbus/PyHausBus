import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 39
  FUNCTION_ID = 128

  def __init__(self,lowerThreshold:int, upperThreshold:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    self.lowerThreshold=lowerThreshold
    self.upperThreshold=upperThreshold
    self.reportTimeBase=reportTimeBase
    self.minReportTime=minReportTime
    self.maxReportTime=maxReportTime
    self.hysteresis=hysteresis
    self.calibration=calibration
    self.deltaSensorID=deltaSensorID


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Configuration(lowerThreshold={self.lowerThreshold}, upperThreshold={self.upperThreshold}, reportTimeBase={self.reportTimeBase}, minReportTime={self.minReportTime}, maxReportTime={self.maxReportTime}, hysteresis={self.hysteresis}, calibration={self.calibration}, deltaSensorID={self.deltaSensorID})"

  '''
  @param lowerThreshold untere Helligkeitsschwelle.
  '''
  def getLowerThreshold(self):
    return self.lowerThreshold

  '''
  @param upperThreshold obere Helligkeitsschwelle.
  '''
  def getUpperThreshold(self):
    return self.upperThreshold

  '''
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  '''
  def getReportTimeBase(self):
    return self.reportTimeBase

  '''
  @param minReportTime Mindestzeit.
  '''
  def getMinReportTime(self):
    return self.minReportTime

  '''
  @param maxReportTime Maximalzeit.
  '''
  def getMaxReportTime(self):
    return self.maxReportTime

  '''
  @param hysteresis Hysterese [10 lux].
  '''
  def getHysteresis(self):
    return self.hysteresis

  '''
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [10 lux].
  '''
  def getCalibration(self):
    return self.calibration

  '''
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  '''
  def getDeltaSensorID(self):
    return self.deltaSensorID



