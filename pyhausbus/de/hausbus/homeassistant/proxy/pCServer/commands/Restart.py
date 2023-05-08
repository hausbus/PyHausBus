import pyhausbus.HausBusUtils as HausBusUtils

class Restart:
  CLASS_ID = 1
  FUNCTION_ID = 12

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Restart()

  def __str__(self):
    return f"Restart()"



