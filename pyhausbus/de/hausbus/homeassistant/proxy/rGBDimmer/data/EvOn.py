import pyhausbus.HausBusUtils as HausBusUtils

class EvOn:
  CLASS_ID = 22
  FUNCTION_ID = 201

  def __init__(self,brightnessRed:int, brightnessGreen:int, brightnessBlue:int, duration:int):
    self.brightnessRed=brightnessRed
    self.brightnessGreen=brightnessGreen
    self.brightnessBlue=brightnessBlue
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOn(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvOn(brightnessRed={self.brightnessRed}, brightnessGreen={self.brightnessGreen}, brightnessBlue={self.brightnessBlue}, duration={self.duration})"

  '''
  @param brightnessRed Helligkeit ROT-Anteil. \r\n0: AUS\r\n100: MAX.
  '''
  def getBrightnessRed(self):
    return self.brightnessRed

  '''
  @param brightnessGreen Helligkeit GRUEN-Anteil. \r\n0: AUS\r\n100: MAX.
  '''
  def getBrightnessGreen(self):
    return self.brightnessGreen

  '''
  @param brightnessBlue Helligkeit BLAU-Anteil. \r\n0: AUS\r\n100: MAX.
  '''
  def getBrightnessBlue(self):
    return self.brightnessBlue

  '''
  @param duration Einschaltdauer in Sekunden.
  '''
  def getDuration(self):
    return self.duration



