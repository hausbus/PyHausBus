import pyhausbus.HausBusUtils as HausBusUtils

class EvLight:
  CLASS_ID = 39
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvLight()

  def __str__(self):
    return f"EvLight()"



