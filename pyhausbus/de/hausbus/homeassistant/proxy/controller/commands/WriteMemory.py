import pyhausbus.HausBusUtils as HausBusUtils

class WriteMemory:
  CLASS_ID = 0
  FUNCTION_ID = 8

  def __init__(self,address:int, data:bytearray):
    self.address=address
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return WriteMemory(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"WriteMemory(address={self.address}, data={self.data})"

  '''
  @param address .
  '''
  def getAddress(self):
    return self.address

  '''
  @param data .
  '''
  def getData(self):
    return self.data



