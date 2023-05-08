import pyhausbus.HausBusUtils as HausBusUtils

class WriteRules:
  CLASS_ID = 0
  FUNCTION_ID = 9

  def __init__(self,offset:int, data:bytearray):
    self.offset=offset
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return WriteRules(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"WriteRules(offset={self.offset}, data={self.data})"

  '''
  @param offset aktueller Offset im Gesamtregelblock.
  '''
  def getOffset(self):
    return self.offset

  '''
  @param data .
  '''
  def getData(self):
    return self.data



