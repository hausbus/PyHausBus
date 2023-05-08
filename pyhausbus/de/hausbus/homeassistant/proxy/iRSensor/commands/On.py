import pyhausbus.HausBusUtils as HausBusUtils

class On:
  CLASS_ID = 33
  FUNCTION_ID = 1

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return On()

  def __str__(self):
    return f"On()"



