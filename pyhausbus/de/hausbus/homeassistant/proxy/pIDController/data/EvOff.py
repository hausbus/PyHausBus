import pyhausbus.HausBusUtils as HausBusUtils

class EvOff:
  CLASS_ID = 44
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOff()

  def __str__(self):
    return f"EvOff()"



