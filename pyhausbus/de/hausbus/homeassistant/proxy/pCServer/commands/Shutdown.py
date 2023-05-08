import pyhausbus.HausBusUtils as HausBusUtils

class Shutdown:
  CLASS_ID = 1
  FUNCTION_ID = 11

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Shutdown()

  def __str__(self):
    return f"Shutdown()"



