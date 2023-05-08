import pyhausbus.HausBusUtils as HausBusUtils

class Off:
  CLASS_ID = 33
  FUNCTION_ID = 0

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Off()

  def __str__(self):
    return f"Off()"



