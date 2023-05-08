from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 19
  FUNCTION_ID = 1

  def __init__(self,maxOnTime:int, offDelayTime:int, timeBase:int, options:MOptions, disableBitIndex:int):
    self.maxOnTime=maxOnTime
    self.offDelayTime=offDelayTime
    self.timeBase=timeBase
    self.options=options
    self.disableBitIndex=disableBitIndex


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), MOptions._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(maxOnTime={self.maxOnTime}, offDelayTime={self.offDelayTime}, timeBase={self.timeBase}, options={self.options}, disableBitIndex={self.disableBitIndex})"

  '''
  @param maxOnTime Maximale Zeit.
  '''
  def getMaxOnTime(self):
    return self.maxOnTime

  '''
  @param offDelayTime Verzoegerungszeit nach einem Off-Kommando.
  '''
  def getOffDelayTime(self):
    return self.offDelayTime

  '''
  @param timeBase Zeitbasis [ms] fuer die Zeitabhaengigen Befehle.
  '''
  def getTimeBase(self):
    return self.timeBase

  '''
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  '''
  def getOptions(self) -> MOptions:
    return self.options

  '''
  @param disableBitIndex Bit Index0-31 Systemvariable.
  '''
  def getDisableBitIndex(self):
    return self.disableBitIndex



