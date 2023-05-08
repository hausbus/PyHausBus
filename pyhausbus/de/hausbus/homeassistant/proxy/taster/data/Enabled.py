import pyhausbus.HausBusUtils as HausBusUtils

class Enabled:
  CLASS_ID = 16
  FUNCTION_ID = 130

  def __init__(self,enabled:int):
    self.enabled=enabled


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Enabled(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Enabled(enabled={self.enabled})"

  '''
  @param enabled 0: Events sind deaktviert\r\n1: Events sind aktiviert.
  '''
  def getEnabled(self):
    return self.enabled



