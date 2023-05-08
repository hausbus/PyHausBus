import pyhausbus.HausBusUtils as HausBusUtils

class Current:
  CLASS_ID = 90
  FUNCTION_ID = 128

  def __init__(self,current:int):
    self.current=current


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Current(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"Current(current={self.current})"

  '''
  @param current verbrauchter Strom in Wattstunden.
  '''
  def getCurrent(self):
    return self.current



