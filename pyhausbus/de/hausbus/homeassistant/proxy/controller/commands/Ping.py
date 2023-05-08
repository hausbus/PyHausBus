import pyhausbus.HausBusUtils as HausBusUtils

class Ping:
  CLASS_ID = 0
  FUNCTION_ID = 127

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Ping()

  def __str__(self):
    return f"Ping()"



