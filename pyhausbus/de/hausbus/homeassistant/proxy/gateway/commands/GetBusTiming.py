import pyhausbus.HausBusUtils as HausBusUtils

class GetBusTiming:
  CLASS_ID = 176
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetBusTiming()

  def __str__(self):
    return f"GetBusTiming()"



