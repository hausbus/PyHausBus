import pyhausbus.HausBusUtils as HausBusUtils

class LastData:
  CLASS_ID = 43
  FUNCTION_ID = 130

  def __init__(self,tagID:int, logicalTagId:int):
    self.tagID=tagID
    self.logicalTagId=logicalTagId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return LastData(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"LastData(tagID={self.tagID}, logicalTagId={self.logicalTagId})"

  '''
  @param tagID last tagID read successfully.
  '''
  def getTagID(self):
    return self.tagID

  '''
  @param logicalTagId falls tagID in der Mapping-Tabelle steht.
  '''
  def getLogicalTagId(self):
    return self.logicalTagId



