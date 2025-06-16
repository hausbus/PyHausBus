from pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class EvStatus:
  CLASS_ID = 36
  FUNCTION_ID = 203

  def __init__(self,value:int, lastEvent:ELastEvent):
    self.value=value
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStatus(HausBusUtils.bytesToWord(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvStatus(value={self.value}, lastEvent={self.lastEvent})"

  '''
  @param value .
  '''
  def getValue(self):
    return self.value

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



