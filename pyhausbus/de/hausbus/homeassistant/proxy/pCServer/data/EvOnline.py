import pyhausbus.HausBusUtils as HausBusUtils

class EvOnline:
  CLASS_ID = 1
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOnline()

  def __str__(self):
    return f"EvOnline()"



