import pyhausbus.HausBusUtils as HausBusUtils

class MoveToPosition:
  CLASS_ID = 18
  FUNCTION_ID = 2

  def __init__(self,position:int):
    self.position=position


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return MoveToPosition(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"MoveToPosition(position={self.position})"

  '''
  @param position in Prozent.
  '''
  def getPosition(self):
    return self.position



