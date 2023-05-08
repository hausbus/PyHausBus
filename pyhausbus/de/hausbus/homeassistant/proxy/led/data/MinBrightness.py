import pyhausbus.HausBusUtils as HausBusUtils

class MinBrightness:
  CLASS_ID = 21
  FUNCTION_ID = 130

  def __init__(self,minBrightness:int):
    self.minBrightness=minBrightness


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return MinBrightness(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"MinBrightness(minBrightness={self.minBrightness})"

  '''
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  '''
  def getMinBrightness(self):
    return self.minBrightness



