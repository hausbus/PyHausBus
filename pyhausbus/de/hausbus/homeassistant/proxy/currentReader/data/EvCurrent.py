import pyhausbus.HausBusUtils as HausBusUtils

class EvCurrent:
  CLASS_ID = 90
  FUNCTION_ID = 201

  def __init__(self,current:int):
    self.current=current


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvCurrent(HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"EvCurrent(current={self.current})"

  '''
  @param current Verbrauchter Strom in Wattstunden.
  '''
  def getCurrent(self):
    return self.current



