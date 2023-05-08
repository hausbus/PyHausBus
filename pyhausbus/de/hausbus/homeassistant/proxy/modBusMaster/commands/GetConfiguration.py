import pyhausbus.HausBusUtils as HausBusUtils

class GetConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 0

  def __init__(self,idx:int):
    self.idx=idx


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetConfiguration(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetConfiguration(idx={self.idx})"

  '''
  @param idx index of the configuration slot.
  '''
  def getIdx(self):
    return self.idx



