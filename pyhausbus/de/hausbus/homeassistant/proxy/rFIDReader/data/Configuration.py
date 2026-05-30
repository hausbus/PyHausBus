import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 43
  FUNCTION_ID = 128

  def __init__(self,readerId:int):
    self.readerId=readerId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Configuration(readerId={self.readerId})"

  '''
  @param readerId logische TagId dieser Instanz.
  '''
  def getReaderId(self):
    return self.readerId



