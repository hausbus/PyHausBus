import pyhausbus.HausBusUtils as HausBusUtils

class EvOpen:
  CLASS_ID = 18
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvOpen()

  def __str__(self):
    return f"EvOpen()"



