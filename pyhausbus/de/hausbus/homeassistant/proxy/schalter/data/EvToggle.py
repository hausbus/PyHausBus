import pyhausbus.HausBusUtils as HausBusUtils

class EvToggle:
  CLASS_ID = 19
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvToggle()

  def __str__(self):
    return f"EvToggle()"



