import pyhausbus.HausBusUtils as HausBusUtils

class EvAbove:
  CLASS_ID = 42
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvAbove()

  def __str__(self):
    return f"EvAbove()"



