import pyhausbus.HausBusUtils as HausBusUtils

class SignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 131

  def __init__(self,signalCount:int):
    self.signalCount=signalCount


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SignalCount(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"SignalCount(signalCount={self.signalCount})"

  '''
  @param signalCount Anzahl gez?hlter S0 Signale seit dem letzten Zur?cksetzen.
  '''
  def getSignalCount(self):
    return self.signalCount



