import pyhausbus.HausBusUtils as HausBusUtils

class EvLow:
  CLASS_ID = 36
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvLow()

  def __str__(self):
    return f"EvLow()"



