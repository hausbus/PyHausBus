import pyhausbus.HausBusUtils as HausBusUtils

class GetStatus:
  CLASS_ID = 16
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetStatus()

  def __str__(self):
    return f"GetStatus()"



