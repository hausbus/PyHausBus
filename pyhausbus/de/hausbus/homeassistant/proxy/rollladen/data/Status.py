import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 18
  FUNCTION_ID = 129

  def __init__(self,position:int):
    self.position=position


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Status(position={self.position})"

  '''
  @param position .
  '''
  def getPosition(self):
    return self.position



