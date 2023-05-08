import pyhausbus.HausBusUtils as HausBusUtils

class EvEnabled:
  CLASS_ID = 16
  FUNCTION_ID = 206

  def __init__(self,enabled:int):
    self.enabled=enabled


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvEnabled(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvEnabled(enabled={self.enabled})"

  '''
  @param enabled 0: Events wurden gerade deaktiviert\r\n1: Events wurden gerade aktiviert.
  '''
  def getEnabled(self):
    return self.enabled



