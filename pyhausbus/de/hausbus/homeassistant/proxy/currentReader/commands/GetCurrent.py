import pyhausbus.HausBusUtils as HausBusUtils

class GetCurrent:
  CLASS_ID = 90
  FUNCTION_ID = 1

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetCurrent()

  def __str__(self):
    return f"GetCurrent()"



