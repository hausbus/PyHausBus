import pyhausbus.HausBusUtils as HausBusUtils

class GetTime:
  CLASS_ID = 3
  FUNCTION_ID = 0

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetTime()

  def __str__(self):
    return f"GetTime()"



