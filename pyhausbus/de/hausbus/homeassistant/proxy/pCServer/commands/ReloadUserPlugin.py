import pyhausbus.HausBusUtils as HausBusUtils

class ReloadUserPlugin:
  CLASS_ID = 1
  FUNCTION_ID = 13

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ReloadUserPlugin()

  def __str__(self):
    return f"ReloadUserPlugin()"



