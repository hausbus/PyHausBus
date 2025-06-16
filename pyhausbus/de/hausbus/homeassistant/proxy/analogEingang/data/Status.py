import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 36
  FUNCTION_ID = 129

  def __init__(self,value:int):
    self.value=value


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Status(value={self.value})"

  '''
  @param value .
  '''
  def getValue(self):
    return self.value



