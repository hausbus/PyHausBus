import pyhausbus.HausBusUtils as HausBusUtils

class On:
  CLASS_ID = 19
  FUNCTION_ID = 3

  def __init__(self,duration:int, onDelay:int):
    self.duration=duration
    self.onDelay=onDelay


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return On(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"On(duration={self.duration}, onDelay={self.onDelay})"

  '''
  @param duration Einschaltdauer: \r\nWert * Zeitbasis [ms]\r\n0=nicht mehr ausschalten.
  '''
  def getDuration(self):
    return self.duration

  '''
  @param onDelay Einschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  '''
  def getOnDelay(self):
    return self.onDelay



