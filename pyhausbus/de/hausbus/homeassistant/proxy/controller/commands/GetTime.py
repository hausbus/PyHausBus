import pyhausbus.HausBusUtils as HausBusUtils

class GetTime:
  CLASS_ID = 0
  FUNCTION_ID = 126

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetTime()

  def __str__(self):
    return f"GetTime()"



