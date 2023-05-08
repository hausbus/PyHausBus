import pyhausbus.HausBusUtils as HausBusUtils

class EvInterrupt:
  CLASS_ID = 90
  FUNCTION_ID = 211

  def __init__(self,value:int, stamp:int):
    self.value=value
    self.stamp=stamp


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvInterrupt(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"EvInterrupt(value={self.value}, stamp={self.stamp})"

  '''
  @param value .
  '''
  def getValue(self):
    return self.value

  '''
  @param stamp .
  '''
  def getStamp(self):
    return self.stamp



