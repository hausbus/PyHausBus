import pyhausbus.HausBusUtils as HausBusUtils

class EvCold:
  CLASS_ID = 32
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvCold()

  def __str__(self):
    return f"EvCold()"



