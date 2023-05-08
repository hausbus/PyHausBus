import pyhausbus.HausBusUtils as HausBusUtils

class EvOff:
  CLASS_ID = 20
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOff()

  def __str__(self):
    return f"EvOff()"



