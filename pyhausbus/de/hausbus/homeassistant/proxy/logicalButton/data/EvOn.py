import pyhausbus.HausBusUtils as HausBusUtils

class EvOn:
  CLASS_ID = 20
  FUNCTION_ID = 201

  def __init__(self,brightness:int):
    self.brightness=brightness


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOn(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvOn(brightness={self.brightness})"

  '''
  @param brightness 0-100% Helligkeit.
  '''
  def getBrightness(self):
    return self.brightness



