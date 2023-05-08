import pyhausbus.HausBusUtils as HausBusUtils

class Power:
  CLASS_ID = 90
  FUNCTION_ID = 130

  def __init__(self,power:int):
    self.power=power


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Power(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Power(power={self.power})"

  '''
  @param power Aktuelle Leistung in Watt.
  '''
  def getPower(self):
    return self.power



