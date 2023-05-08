import pyhausbus.HausBusUtils as HausBusUtils

class SetBrightness:
  CLASS_ID = 17
  FUNCTION_ID = 2

  def __init__(self,brightness:int, duration:int):
    self.brightness=brightness
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetBrightness(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetBrightness(brightness={self.brightness}, duration={self.duration})"

  '''
  @param brightness Helligkeit in Prozent.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param duration Einschaltdauer in Sekunden.
  '''
  def getDuration(self):
    return self.duration



