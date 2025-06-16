import pyhausbus.HausBusUtils as HausBusUtils

class GetStatus:
  CLASS_ID = 36
  FUNCTION_ID = 2

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetStatus()

  def __str__(self):
    return f"GetStatus()"



