import pyhausbus.HausBusUtils as HausBusUtils

class EvOn:
  CLASS_ID = 33
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOn()

  def __str__(self):
    return f"EvOn()"



