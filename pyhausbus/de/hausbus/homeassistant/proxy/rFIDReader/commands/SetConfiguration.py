import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 43
  FUNCTION_ID = 1

  def __init__(self,readerId:int):
    self.readerId=readerId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(readerId={self.readerId})"

  '''
  @param readerId logische TagID dieser Instanz.
  '''
  def getReaderId(self):
    return self.readerId



