import pyhausbus.HausBusUtils as HausBusUtils

class AllOff:
  CLASS_ID = 160
  FUNCTION_ID = 2

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return AllOff()

  def __str__(self):
    return f"AllOff()"



