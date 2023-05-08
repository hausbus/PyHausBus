import pyhausbus.HausBusUtils as HausBusUtils

class EvGroupUndefined:
  CLASS_ID = 0
  FUNCTION_ID = 204

  def __init__(self,index:int, status:int):
    self.index=index
    self.status=status


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvGroupUndefined(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvGroupUndefined(index={self.index}, status={self.status})"

  '''
  @param index Gruppenindex.
  '''
  def getIndex(self):
    return self.index

  '''
  @param status Status der Bits in der logischen Gruppe..
  '''
  def getStatus(self):
    return self.status



