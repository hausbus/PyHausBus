import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 41
  FUNCTION_ID = 1

  def __init__(self,lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    self.lowerThreshold=lowerThreshold
    self.lowerThresholdFraction=lowerThresholdFraction
    self.upperThreshold=upperThreshold
    self.upperThresholdFraction=upperThresholdFraction
    self.reportTimeBase=reportTimeBase
    self.minReportTime=minReportTime
    self.maxReportTime=maxReportTime
    self.hysteresis=hysteresis
    self.calibration=calibration
    self.deltaSensorID=deltaSensorID


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(lowerThreshold={self.lowerThreshold}, lowerThresholdFraction={self.lowerThresholdFraction}, upperThreshold={self.upperThreshold}, upperThresholdFraction={self.upperThresholdFraction}, reportTimeBase={self.reportTimeBase}, minReportTime={self.minReportTime}, maxReportTime={self.maxReportTime}, hysteresis={self.hysteresis}, calibration={self.calibration}, deltaSensorID={self.deltaSensorID})"

  '''
  @param lowerThreshold untere Leistungsschwelle[kWh].
  '''
  def getLowerThreshold(self):
    return self.lowerThreshold

  '''
  @param lowerThresholdFraction Nachkommastellen der unteren Leistungsschwelle[00-99].
  '''
  def getLowerThresholdFraction(self):
    return self.lowerThresholdFraction

  '''
  @param upperThreshold obere Leistungsschwelle[kWh].
  '''
  def getUpperThreshold(self):
    return self.upperThreshold

  '''
  @param upperThresholdFraction Nachkommastellen der oberen Leistungsschwelle[00-99].
  '''
  def getUpperThresholdFraction(self):
    return self.upperThresholdFraction

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
  @param hysteresis Hysterese [Wert * 0.
  '''
  def getHysteresis(self):
    return self.hysteresis

  '''
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Prozent].
  '''
  def getCalibration(self):
    return self.calibration

  '''
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  '''
  def getDeltaSensorID(self):
    return self.deltaSensorID



