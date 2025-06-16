from pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 48
  FUNCTION_ID = 129

  def __init__(self,value:int, lastEvent:ELastEvent):
    self.value=value
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToWord(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Status(value={self.value}, lastEvent={self.lastEvent})"

  '''
  @param value aktuell gemessener Druck in Pa.
  '''
  def getValue(self):
    return self.value

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



