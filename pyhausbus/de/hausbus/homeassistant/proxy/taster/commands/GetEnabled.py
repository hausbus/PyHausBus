import pyhausbus.HausBusUtils as HausBusUtils

class GetEnabled:
  CLASS_ID = 16
  FUNCTION_ID = 4

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetEnabled()

  def __str__(self):
    return f"GetEnabled()"



