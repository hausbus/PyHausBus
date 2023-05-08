from pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 39
  FUNCTION_ID = 129

  def __init__(self,brightness:int, lastEvent:ELastEvent):
    self.brightness=brightness
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToWord(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Status(brightness={self.brightness}, lastEvent={self.lastEvent})"

  '''
  @param brightness Helligkeitswert.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



