import pyhausbus.HausBusUtils as HausBusUtils

class EvStatus:
  CLASS_ID = 35
  FUNCTION_ID = 200

  def __init__(self,counter:int, fraction:int):
    self.counter=counter
    self.fraction=fraction


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStatus(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvStatus(counter={self.counter}, fraction={self.fraction})"

  '''
  @param counter Zaehler ganze Einheiten.
  '''
  def getCounter(self):
    return self.counter

  '''
  @param fraction Bruchteil 0-scaleFactor.
  '''
  def getFraction(self):
    return self.fraction



