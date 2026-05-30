import pyhausbus.HausBusUtils as HausBusUtils

class SetTagMapping:
  CLASS_ID = 43
  FUNCTION_ID = 4

  def __init__(self,idx:int, physicalTagId:int, logicalTagId:int):
    self.idx=idx
    self.physicalTagId=physicalTagId
    self.logicalTagId=logicalTagId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetTagMapping(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetTagMapping(idx={self.idx}, physicalTagId={self.physicalTagId}, logicalTagId={self.logicalTagId})"

  '''
  @param idx index in der Mapping-Tabelle.
  '''
  def getIdx(self):
    return self.idx

  '''
  @param physicalTagId Wenn diese TagId gelesen wird.
  '''
  def getPhysicalTagId(self):
    return self.physicalTagId

  '''
  @param logicalTagId logische TagId.
  '''
  def getLogicalTagId(self):
    return self.logicalTagId



