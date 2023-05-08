import pyhausbus.HausBusUtils as HausBusUtils

class CheckBusTiming:
  CLASS_ID = 176
  FUNCTION_ID = 2

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return CheckBusTiming()

  def __str__(self):
    return f"CheckBusTiming()"



