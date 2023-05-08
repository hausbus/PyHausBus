import pyhausbus.HausBusUtils as HausBusUtils

class SetSignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 2

  def __init__(self,signalCount:int):
    self.signalCount=signalCount


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetSignalCount(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"SetSignalCount(signalCount={self.signalCount})"

  '''
  @param signalCount .
  '''
  def getSignalCount(self):
    return self.signalCount



