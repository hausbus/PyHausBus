import pyhausbus.HausBusUtils as HausBusUtils

class UnitGroupStatus:
  CLASS_ID = 0
  FUNCTION_ID = 138

  def __init__(self,index:int, status:int):
    self.index=index
    self.status=status


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return UnitGroupStatus(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"UnitGroupStatus(index={self.index}, status={self.status})"

  '''
  @param index Index der logischen Gruppe in diesem Controller.
  '''
  def getIndex(self):
    return self.index

  '''
  @param status Status der Bits in der logischen Gruppe..
  '''
  def getStatus(self):
    return self.status



