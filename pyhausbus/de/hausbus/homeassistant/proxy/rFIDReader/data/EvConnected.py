import pyhausbus.HausBusUtils as HausBusUtils

class EvConnected:
  CLASS_ID = 43
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvConnected()

  def __str__(self):
    return f"EvConnected()"



