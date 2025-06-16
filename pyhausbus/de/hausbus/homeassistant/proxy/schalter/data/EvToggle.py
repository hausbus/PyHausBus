import pyhausbus.HausBusUtils as HausBusUtils

class EvToggle:
  CLASS_ID = 19
  FUNCTION_ID = 202

  def __init__(self,offTime:int, onTime:int, quantity:int):
    self.offTime=offTime
    self.onTime=onTime
    self.quantity=quantity


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvToggle(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvToggle(offTime={self.offTime}, onTime={self.onTime}, quantity={self.quantity})"

  '''
  @param offTime Dauer der Aus-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  '''
  def getOffTime(self):
    return self.offTime

  '''
  @param onTime Dauer der An-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  '''
  def getOnTime(self):
    return self.onTime

  '''
  @param quantity Anzahl der Schaltvorgaenge.
  '''
  def getQuantity(self):
    return self.quantity



