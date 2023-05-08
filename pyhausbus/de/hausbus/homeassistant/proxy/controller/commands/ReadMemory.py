import pyhausbus.HausBusUtils as HausBusUtils

class ReadMemory:
  CLASS_ID = 0
  FUNCTION_ID = 7

  def __init__(self,address:int, length:int):
    self.address=address
    self.length=length


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ReadMemory(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"ReadMemory(address={self.address}, length={self.length})"

  '''
  @param address .
  '''
  def getAddress(self):
    return self.address

  '''
  @param length .
  '''
  def getLength(self):
    return self.length



