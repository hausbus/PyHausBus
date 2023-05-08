import pyhausbus.HausBusUtils as HausBusUtils

class GetLastData:
  CLASS_ID = 43
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetLastData()

  def __str__(self):
    return f"GetLastData()"



