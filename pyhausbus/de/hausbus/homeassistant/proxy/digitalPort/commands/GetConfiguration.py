import pyhausbus.HausBusUtils as HausBusUtils

class GetConfiguration:
  CLASS_ID = 15
  FUNCTION_ID = 0

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetConfiguration()

  def __str__(self):
    return f"GetConfiguration()"



