import pyhausbus.HausBusUtils as HausBusUtils

class GetPower:
  CLASS_ID = 90
  FUNCTION_ID = 5

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetPower()

  def __str__(self):
    return f"GetPower()"



