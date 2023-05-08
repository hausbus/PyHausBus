import pyhausbus.HausBusUtils as HausBusUtils

class GetConfiguration:
  CLASS_ID = 90
  FUNCTION_ID = 4

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetConfiguration()

  def __str__(self):
    return f"GetConfiguration()"



