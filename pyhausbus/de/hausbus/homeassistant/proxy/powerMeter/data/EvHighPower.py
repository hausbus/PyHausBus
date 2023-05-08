import pyhausbus.HausBusUtils as HausBusUtils

class EvHighPower:
  CLASS_ID = 41
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvHighPower()

  def __str__(self):
    return f"EvHighPower()"



