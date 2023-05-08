import pyhausbus.HausBusUtils as HausBusUtils

class EvConfortable:
  CLASS_ID = 34
  FUNCTION_ID = 201

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvConfortable()

  def __str__(self):
    return f"EvConfortable()"



