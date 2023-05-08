import pyhausbus.HausBusUtils as HausBusUtils

class EvDisabled:
  CLASS_ID = 19
  FUNCTION_ID = 204

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDisabled()

  def __str__(self):
    return f"EvDisabled()"



