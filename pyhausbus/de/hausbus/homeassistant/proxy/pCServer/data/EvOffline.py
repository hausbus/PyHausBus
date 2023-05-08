import pyhausbus.HausBusUtils as HausBusUtils

class EvOffline:
  CLASS_ID = 1
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOffline()

  def __str__(self):
    return f"EvOffline()"



