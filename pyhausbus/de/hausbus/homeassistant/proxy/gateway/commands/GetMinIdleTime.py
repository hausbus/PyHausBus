import pyhausbus.HausBusUtils as HausBusUtils

class GetMinIdleTime:
  CLASS_ID = 176
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetMinIdleTime()

  def __str__(self):
    return f"GetMinIdleTime()"



