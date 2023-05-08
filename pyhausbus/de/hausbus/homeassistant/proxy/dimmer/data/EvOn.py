import pyhausbus.HausBusUtils as HausBusUtils

class EvOn:
  CLASS_ID = 17
  FUNCTION_ID = 201

  def __init__(self,brightness:int, duration:int):
    self.brightness=brightness
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOn(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvOn(brightness={self.brightness}, duration={self.duration})"

  '''
  @param brightness aktuelle Helligkeit 0-100%.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param duration Einschaltdauer: Wert in Sekunden\r\n0=Endlos.
  '''
  def getDuration(self):
    return self.duration



