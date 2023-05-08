import pyhausbus.HausBusUtils as HausBusUtils

class ClearSignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 7

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ClearSignalCount()

  def __str__(self):
    return f"ClearSignalCount()"



