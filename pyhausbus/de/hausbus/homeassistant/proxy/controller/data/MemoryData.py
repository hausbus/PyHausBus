import pyhausbus.HausBusUtils as HausBusUtils

class MemoryData:
  CLASS_ID = 0
  FUNCTION_ID = 132

  def __init__(self,address:int, data:bytearray):
    self.address=address
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return MemoryData(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"MemoryData(address={self.address}, data={self.data})"

  '''
  @param address Adresse des gemeldeten Speicherinhaltes.
  '''
  def getAddress(self):
    return self.address

  '''
  @param data Daten....
  '''
  def getData(self):
    return self.data



