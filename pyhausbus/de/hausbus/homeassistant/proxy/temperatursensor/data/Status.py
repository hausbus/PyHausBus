from pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 32
  FUNCTION_ID = 129

  def __init__(self,celsius:int, centiCelsius:int, lastEvent:ELastEvent):
    self.celsius=celsius
    self.centiCelsius=centiCelsius
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Status(celsius={self.celsius}, centiCelsius={self.centiCelsius}, lastEvent={self.lastEvent})"

  '''
  @param celsius Grad Celsius.
  '''
  def getCelsius(self):
    return self.celsius

  '''
  @param centiCelsius hundertstel Grad Celsius.
  '''
  def getCentiCelsius(self):
    return self.centiCelsius

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



