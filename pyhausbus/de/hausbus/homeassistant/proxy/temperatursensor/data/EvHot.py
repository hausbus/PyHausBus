import pyhausbus.HausBusUtils as HausBusUtils

class EvHot:
  CLASS_ID = 32
  FUNCTION_ID = 202

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvHot()

  def __str__(self):
    return f"EvHot()"



