import pyhausbus.HausBusUtils as HausBusUtils

class EvHigh:
  CLASS_ID = 48
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvHigh()

  def __str__(self):
    return f"EvHigh()"



