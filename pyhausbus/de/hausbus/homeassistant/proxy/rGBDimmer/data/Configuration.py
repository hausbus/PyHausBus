import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 22
  FUNCTION_ID = 128

  def __init__(self,fadingTime:int):
    self.fadingTime=fadingTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Configuration(fadingTime={self.fadingTime})"

  '''
  @param fadingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu schalten.
  '''
  def getFadingTime(self):
    return self.fadingTime



