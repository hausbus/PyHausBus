import pyhausbus.HausBusUtils as HausBusUtils

class On:
  CLASS_ID = 21
  FUNCTION_ID = 3

  def __init__(self,brightness:int, duration:int, onDelay:int):
    self.brightness=brightness
    self.duration=duration
    self.onDelay=onDelay


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return On(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"On(brightness={self.brightness}, duration={self.duration}, onDelay={self.onDelay})"

  '''
  @param brightness 0-100% Helligkeit.
  '''
  def getBrightness(self):
    return self.brightness

  '''
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  '''
  def getDuration(self):
    return self.duration

  '''
  @param onDelay Einschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  '''
  def getOnDelay(self):
    return self.onDelay



