import pyhausbus.HausBusUtils as HausBusUtils

class EvDay:
  CLASS_ID = 0
  FUNCTION_ID = 206

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDay()

  def __str__(self):
    return f"EvDay()"



