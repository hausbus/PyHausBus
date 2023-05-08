import pyhausbus.HausBusUtils as HausBusUtils

class EvWarm:
  CLASS_ID = 32
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvWarm()

  def __str__(self):
    return f"EvWarm()"



