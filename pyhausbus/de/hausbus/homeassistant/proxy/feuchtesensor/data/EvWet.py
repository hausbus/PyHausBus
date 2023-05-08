import pyhausbus.HausBusUtils as HausBusUtils

class EvWet:
  CLASS_ID = 34
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvWet()

  def __str__(self):
    return f"EvWet()"



