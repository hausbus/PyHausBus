import pyhausbus.HausBusUtils as HausBusUtils

class EvMediumPower:
  CLASS_ID = 41
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvMediumPower()

  def __str__(self):
    return f"EvMediumPower()"



