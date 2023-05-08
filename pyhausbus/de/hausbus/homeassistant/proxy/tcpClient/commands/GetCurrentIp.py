import pyhausbus.HausBusUtils as HausBusUtils

class GetCurrentIp:
  CLASS_ID = 91
  FUNCTION_ID = 2

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetCurrentIp()

  def __str__(self):
    return f"GetCurrentIp()"



