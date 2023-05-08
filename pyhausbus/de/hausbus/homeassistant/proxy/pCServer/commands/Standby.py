import pyhausbus.HausBusUtils as HausBusUtils

class Standby:
  CLASS_ID = 1
  FUNCTION_ID = 10

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Standby()

  def __str__(self):
    return f"Standby()"



