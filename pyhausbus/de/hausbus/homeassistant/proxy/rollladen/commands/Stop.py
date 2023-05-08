import pyhausbus.HausBusUtils as HausBusUtils

class Stop:
  CLASS_ID = 18
  FUNCTION_ID = 4

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Stop()

  def __str__(self):
    return f"Stop()"



