import pyhausbus.HausBusUtils as HausBusUtils

class EvOn:
  CLASS_ID = 19
  FUNCTION_ID = 201

  def __init__(self,duration:int):
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOn(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvOn(duration={self.duration})"

  '''
  @param duration Dauer.
  '''
  def getDuration(self):
    return self.duration



