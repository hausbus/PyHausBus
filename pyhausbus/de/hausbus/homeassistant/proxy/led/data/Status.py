import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 21
  FUNCTION_ID = 129

  def __init__(self,brightness:int, duration:int):
    self.brightness=brightness
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Status(brightness={self.brightness}, duration={self.duration})"

  '''
  @param brightness Helligkeit der LED.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  '''
  def getDuration(self):
    return self.duration



