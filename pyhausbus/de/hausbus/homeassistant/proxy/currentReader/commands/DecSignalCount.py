import pyhausbus.HausBusUtils as HausBusUtils

class DecSignalCount:
  CLASS_ID = 90
  FUNCTION_ID = 10

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return DecSignalCount()

  def __str__(self):
    return f"DecSignalCount()"



