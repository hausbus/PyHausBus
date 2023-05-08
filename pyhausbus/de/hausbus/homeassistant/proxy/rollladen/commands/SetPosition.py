import pyhausbus.HausBusUtils as HausBusUtils

class SetPosition:
  CLASS_ID = 18
  FUNCTION_ID = 6

  def __init__(self,position:int):
    self.position=position


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetPosition(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetPosition(position={self.position})"

  '''
  @param position Aktuelle Position setzen 0-100% geschlossen.
  '''
  def getPosition(self):
    return self.position



