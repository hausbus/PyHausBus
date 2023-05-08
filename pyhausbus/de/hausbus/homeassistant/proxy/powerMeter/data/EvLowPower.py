import pyhausbus.HausBusUtils as HausBusUtils

class EvLowPower:
  CLASS_ID = 41
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvLowPower()

  def __str__(self):
    return f"EvLowPower()"



