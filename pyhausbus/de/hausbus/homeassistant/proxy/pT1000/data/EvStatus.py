from pyhausbus.de.hausbus.homeassistant.proxy.pT1000.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class EvStatus:
  CLASS_ID = 49
  FUNCTION_ID = 203

  def __init__(self,celsius:int, lastEvent:ELastEvent):
    self.celsius=celsius
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStatus(HausBusUtils.bytesToWord(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvStatus(celsius={self.celsius}, lastEvent={self.lastEvent})"

  '''
  @param celsius Grad Celsius.
  '''
  def getCelsius(self):
    return self.celsius

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



