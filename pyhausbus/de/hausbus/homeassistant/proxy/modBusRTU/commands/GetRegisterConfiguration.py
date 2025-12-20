import pyhausbus.HausBusUtils as HausBusUtils

class GetRegisterConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 2

  def __init__(self,idx:int):
    self.idx=idx


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetRegisterConfiguration(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetRegisterConfiguration(idx={self.idx})"

  '''
  @param idx index of the configuration slot.
  '''
  def getIdx(self):
    return self.idx



