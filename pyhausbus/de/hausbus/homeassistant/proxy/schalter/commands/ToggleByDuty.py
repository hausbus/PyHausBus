import pyhausbus.HausBusUtils as HausBusUtils

class ToggleByDuty:
  CLASS_ID = 19
  FUNCTION_ID = 6

  def __init__(self,duty:int, quantity:int):
    self.duty=duty
    self.quantity=quantity


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ToggleByDuty(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"ToggleByDuty(duty={self.duty}, quantity={self.quantity})"

  '''
  @param duty 0-100% Pulsverh?ltnis.
  '''
  def getDuty(self):
    return self.duty

  '''
  @param quantity Anzahl der Zustandswechsel.
  '''
  def getQuantity(self):
    return self.quantity



