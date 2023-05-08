from pyhausbus.de.hausbus.homeassistant.proxy.led.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 21
  FUNCTION_ID = 1

  def __init__(self,dimmOffset:int, minBrightness:int, timeBase:int, options:MOptions):
    self.dimmOffset=dimmOffset
    self.minBrightness=minBrightness
    self.timeBase=timeBase
    self.options=options


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), MOptions._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(dimmOffset={self.dimmOffset}, minBrightness={self.minBrightness}, timeBase={self.timeBase}, options={self.options})"

  '''
  @param dimmOffset 0-100% offset auf den im Kommando angegebenen Helligkeitswert.
  '''
  def getDimmOffset(self):
    return self.dimmOffset

  '''
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  '''
  def getMinBrightness(self):
    return self.minBrightness

  '''
  @param timeBase Zeitbasis [ms] fuer Zeitabhaengige Befehle..
  '''
  def getTimeBase(self):
    return self.timeBase

  '''
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  '''
  def getOptions(self) -> MOptions:
    return self.options



