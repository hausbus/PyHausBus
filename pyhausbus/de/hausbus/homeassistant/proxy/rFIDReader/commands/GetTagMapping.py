import pyhausbus.HausBusUtils as HausBusUtils

class GetTagMapping:
  CLASS_ID = 43
  FUNCTION_ID = 5

  def __init__(self,idx:int):
    self.idx=idx


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetTagMapping(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetTagMapping(idx={self.idx})"

  '''
  @param idx index in der Mapping-Tabelle.
  '''
  def getIdx(self):
    return self.idx



