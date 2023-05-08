import pyhausbus.HausBusUtils as HausBusUtils

class SetMinBrightness:
  CLASS_ID = 20
  FUNCTION_ID = 6

  def __init__(self,minBrightness:int):
    self.minBrightness=minBrightness


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetMinBrightness(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetMinBrightness(minBrightness={self.minBrightness})"

  '''
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  '''
  def getMinBrightness(self):
    return self.minBrightness



