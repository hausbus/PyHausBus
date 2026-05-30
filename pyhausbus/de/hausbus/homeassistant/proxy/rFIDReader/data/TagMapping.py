import pyhausbus.HausBusUtils as HausBusUtils

class TagMapping:
  CLASS_ID = 43
  FUNCTION_ID = 131

  def __init__(self,idx:int, physicalTagId:int, logicalTagId:int):
    self.idx=idx
    self.physicalTagId=physicalTagId
    self.logicalTagId=logicalTagId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return TagMapping(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"TagMapping(idx={self.idx}, physicalTagId={self.physicalTagId}, logicalTagId={self.logicalTagId})"

  '''
  @param idx Index in der Mapping-Tabelle.
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



