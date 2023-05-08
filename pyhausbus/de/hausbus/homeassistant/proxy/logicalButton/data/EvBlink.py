import pyhausbus.HausBusUtils as HausBusUtils

class EvBlink:
  CLASS_ID = 20
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvBlink()

  def __str__(self):
    return f"EvBlink()"



