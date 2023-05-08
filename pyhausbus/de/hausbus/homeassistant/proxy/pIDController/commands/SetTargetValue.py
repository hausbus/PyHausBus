import pyhausbus.HausBusUtils as HausBusUtils

class SetTargetValue:
  CLASS_ID = 44
  FUNCTION_ID = 2

  def __init__(self,targetValue:int):
    self.targetValue=targetValue


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetTargetValue(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetTargetValue(targetValue={self.targetValue})"

  '''
  @param targetValue Regelungszielwert z.B. targetValue*0.
  '''
  def getTargetValue(self):
    return self.targetValue



