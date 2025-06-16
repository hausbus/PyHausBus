import pyhausbus.HausBusUtils as HausBusUtils

class EvInRange:
  CLASS_ID = 49
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvInRange()

  def __str__(self):
    return f"EvInRange()"



