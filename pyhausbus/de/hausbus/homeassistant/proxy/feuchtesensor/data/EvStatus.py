from pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class EvStatus:
  CLASS_ID = 34
  FUNCTION_ID = 203

  def __init__(self,relativeHumidity:int, centiHumidity:int, lastEvent:ELastEvent):
    self.relativeHumidity=relativeHumidity
    self.centiHumidity=centiHumidity
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStatus(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvStatus(relativeHumidity={self.relativeHumidity}, centiHumidity={self.centiHumidity}, lastEvent={self.lastEvent})"

  '''
  @param relativeHumidity Relative Luftfeuchte in %.
  '''
  def getRelativeHumidity(self):
    return self.relativeHumidity

  '''
  @param centiHumidity hundertstel Relative Luftfeuchte in %.
  '''
  def getCentiHumidity(self):
    return self.centiHumidity

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



