import pyhausbus.HausBusUtils as HausBusUtils

class ReadRules:
  CLASS_ID = 0
  FUNCTION_ID = 10

  def __init__(self,offset:int, length:int):
    self.offset=offset
    self.length=length


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ReadRules(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"ReadRules(offset={self.offset}, length={self.length})"

  '''
  @param offset Offset im Gesamtregelblock.
  '''
  def getOffset(self):
    return self.offset

  '''
  @param length Datenlaenge.
  '''
  def getLength(self):
    return self.length



