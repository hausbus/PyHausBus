import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 43
  FUNCTION_ID = 1

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration()

  def __str__(self):
    return f"SetConfiguration()"



