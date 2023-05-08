import pyhausbus.HausBusUtils as HausBusUtils

class AllOn:
  CLASS_ID = 160
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return AllOn()

  def __str__(self):
    return f"AllOn()"



