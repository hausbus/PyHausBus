import pyhausbus.HausBusUtils as HausBusUtils

class LastData:
  CLASS_ID = 43
  FUNCTION_ID = 130

  def __init__(self,tagID:int):
    self.tagID=tagID


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return LastData(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"LastData(tagID={self.tagID})"

  '''
  @param tagID last tagID read successfully.
  '''
  def getTagID(self):
    return self.tagID



