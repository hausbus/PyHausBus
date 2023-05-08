import pyhausbus.HausBusUtils as HausBusUtils

class EvDark:
  CLASS_ID = 39
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDark()

  def __str__(self):
    return f"EvDark()"



