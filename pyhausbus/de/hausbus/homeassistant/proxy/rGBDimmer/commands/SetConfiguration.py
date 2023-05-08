import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 22
  FUNCTION_ID = 1

  def __init__(self,fadingTime:int):
    self.fadingTime=fadingTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(fadingTime={self.fadingTime})"

  '''
  @param fadingTime Zeit a 50ms um 0-100% zu dimmen.
  '''
  def getFadingTime(self):
    return self.fadingTime



