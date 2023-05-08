import pyhausbus.HausBusUtils as HausBusUtils

class GetState:
  CLASS_ID = 43
  FUNCTION_ID = 2

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetState()

  def __str__(self):
    return f"GetState()"



