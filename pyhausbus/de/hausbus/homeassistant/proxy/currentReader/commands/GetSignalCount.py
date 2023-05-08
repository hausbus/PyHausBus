import pyhausbus.HausBusUtils as HausBusUtils

class GetSignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 6

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetSignalCount()

  def __str__(self):
    return f"GetSignalCount()"



