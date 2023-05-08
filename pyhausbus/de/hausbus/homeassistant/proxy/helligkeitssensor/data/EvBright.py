import pyhausbus.HausBusUtils as HausBusUtils

class EvBright:
  CLASS_ID = 39
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvBright()

  def __str__(self):
    return f"EvBright()"



