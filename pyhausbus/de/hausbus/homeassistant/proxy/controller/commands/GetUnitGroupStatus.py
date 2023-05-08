import pyhausbus.HausBusUtils as HausBusUtils

class GetUnitGroupStatus:
  CLASS_ID = 0
  FUNCTION_ID = 18

  def __init__(self,index:int):
    self.index=index


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetUnitGroupStatus(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetUnitGroupStatus(index={self.index})"

  '''
  @param index Index der logischen Gruppe in diesem Controller.
  '''
  def getIndex(self):
    return self.index



