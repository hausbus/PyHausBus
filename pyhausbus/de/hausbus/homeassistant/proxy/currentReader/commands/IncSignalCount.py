import pyhausbus.HausBusUtils as HausBusUtils

class IncSignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 9

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return IncSignalCount()

  def __str__(self):
    return f"IncSignalCount()"



