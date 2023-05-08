import pyhausbus.HausBusUtils as HausBusUtils

class Blink:
  CLASS_ID = 21
  FUNCTION_ID = 4

  def __init__(self,brightness:int, offTime:int, onTime:int, quantity:int):
    self.brightness=brightness
    self.offTime=offTime
    self.onTime=onTime
    self.quantity=quantity


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Blink(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Blink(brightness={self.brightness}, offTime={self.offTime}, onTime={self.onTime}, quantity={self.quantity})"

  '''
  @param brightness 0-100% Helligkeit.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param offTime Ausschaltdauer: \r\nWert * Zeitbasis [ms].
  '''
  def getOffTime(self):
    return self.offTime

  '''
  @param onTime Einschaltdauer: \r\nWert * Zeitbasis [ms].
  '''
  def getOnTime(self):
    return self.onTime

  '''
  @param quantity Anzahl Blinks.
  '''
  def getQuantity(self):
    return self.quantity



