import pyhausbus.HausBusUtils as HausBusUtils

class Reset:
  CLASS_ID = 0
  FUNCTION_ID = 1

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Reset()

  def __str__(self):
    return f"Reset()"



