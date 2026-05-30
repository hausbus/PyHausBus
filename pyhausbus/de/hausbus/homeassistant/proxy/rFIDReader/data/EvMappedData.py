import pyhausbus.HausBusUtils as HausBusUtils

class EvMappedData:
  CLASS_ID = 43
  FUNCTION_ID = 202

  def __init__(self,logicalTagId:int):
    self.logicalTagId=logicalTagId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvMappedData(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvMappedData(logicalTagId={self.logicalTagId})"

  '''
  @param logicalTagId logische ID wenn die physikalische tagID ein Mapping hat.
  '''
  def getLogicalTagId(self):
    return self.logicalTagId



