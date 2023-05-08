import pyhausbus.HausBusUtils as HausBusUtils

class EvClosed:
  CLASS_ID = 18
  FUNCTION_ID = 200

  def __init__(self,position:int):
    self.position=position


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvClosed(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvClosed(position={self.position})"

  '''
  @param position in Prozent.
  '''
  def getPosition(self):
    return self.position



