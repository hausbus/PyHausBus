import pyhausbus.HausBusUtils as HausBusUtils

class Pong:
  CLASS_ID = 0
  FUNCTION_ID = 199

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Pong()

  def __str__(self):
    return f"Pong()"



