import pyhausbus.HausBusUtils as HausBusUtils

class ResetBusTiming:
  CLASS_ID = 176
  FUNCTION_ID = 4

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ResetBusTiming()

  def __str__(self):
    return f"ResetBusTiming()"



