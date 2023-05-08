import pyhausbus.HausBusUtils as HausBusUtils

class EvData:
  CLASS_ID = 43
  FUNCTION_ID = 201

  def __init__(self,tagID:int):
    self.tagID=tagID


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvData(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"EvData(tagID={self.tagID})"

  '''
  @param tagID ID of the detected RFID tag.
  '''
  def getTagID(self):
    return self.tagID



