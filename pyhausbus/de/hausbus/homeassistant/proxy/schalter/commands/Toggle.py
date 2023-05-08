import pyhausbus.HausBusUtils as HausBusUtils

class Toggle:
  CLASS_ID = 19
  FUNCTION_ID = 4

  def __init__(self,offTime:int, onTime:int, quantity:int):
    self.offTime=offTime
    self.onTime=onTime
    self.quantity=quantity


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Toggle(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Toggle(offTime={self.offTime}, onTime={self.onTime}, quantity={self.quantity})"

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
  @param quantity Anzahl der Zustandswechsel.
  '''
  def getQuantity(self):
    return self.quantity



