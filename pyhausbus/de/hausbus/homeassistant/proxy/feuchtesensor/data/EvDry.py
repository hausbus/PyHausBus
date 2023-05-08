import pyhausbus.HausBusUtils as HausBusUtils

class EvDry:
  CLASS_ID = 34
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDry()

  def __str__(self):
    return f"EvDry()"



