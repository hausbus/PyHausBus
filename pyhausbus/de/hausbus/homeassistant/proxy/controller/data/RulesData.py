import pyhausbus.HausBusUtils as HausBusUtils

class RulesData:
  CLASS_ID = 0
  FUNCTION_ID = 134

  def __init__(self,offset:int, data:bytearray):
    self.offset=offset
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return RulesData(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"RulesData(offset={self.offset}, data={self.data})"

  '''
  @param offset offset im Gesamtregelblock.
  '''
  def getOffset(self):
    return self.offset

  '''
  @param data .
  '''
  def getData(self):
    return self.data



