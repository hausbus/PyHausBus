from pyhausbus.de.hausbus.homeassistant.proxy.currentReader.params.MConfig import MConfig
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 90
  FUNCTION_ID = 3

  def __init__(self,config:MConfig, impPerKwh:int, startCurrent:int, currentReportInterval:int):
    self.config=config
    self.impPerKwh=impPerKwh
    self.startCurrent=startCurrent
    self.currentReportInterval=currentReportInterval


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(MConfig._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(config={self.config}, impPerKwh={self.impPerKwh}, startCurrent={self.startCurrent}, currentReportInterval={self.currentReportInterval})"

  '''
  @param config .
  '''
  def getConfig(self) -> MConfig:
    return self.config

  '''
  @param impPerKwh Anzahl Signale pro kWh.
  '''
  def getImpPerKwh(self):
    return self.impPerKwh

  '''
  @param startCurrent Startwert Stromverbrauch in Wattstunden.
  '''
  def getStartCurrent(self):
    return self.startCurrent

  '''
  @param currentReportInterval Interval in Sekunden nach dem immer der aktuelle Gesamtstromverbrauch gemeldet wird.
  '''
  def getCurrentReportInterval(self):
    return self.currentReportInterval



