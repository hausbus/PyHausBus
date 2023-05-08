import pyhausbus.HausBusUtils as HausBusUtils

class GetMinBrightness:
  CLASS_ID = 20
  FUNCTION_ID = 7

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetMinBrightness()

  def __str__(self):
    return f"GetMinBrightness()"



