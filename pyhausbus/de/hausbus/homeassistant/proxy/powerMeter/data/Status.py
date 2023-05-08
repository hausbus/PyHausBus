from pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.params.ELastEvent import ELastEvent
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 41
  FUNCTION_ID = 129

  def __init__(self,power:int, centiPower:int, lastEvent:ELastEvent):
    self.power=power
    self.centiPower=centiPower
    self.lastEvent=lastEvent


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToSInt(dataIn, offset), HausBusUtils.bytesToSInt(dataIn, offset), ELastEvent._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Status(power={self.power}, centiPower={self.centiPower}, lastEvent={self.lastEvent})"

  '''
  @param power Aktueller Stromverbrauch.
  '''
  def getPower(self):
    return self.power

  '''
  @param centiPower hundertstel Stromverbrauch.
  '''
  def getCentiPower(self):
    return self.centiPower

  '''
  @param lastEvent .
  '''
  def getLastEvent(self):
    return self.lastEvent



