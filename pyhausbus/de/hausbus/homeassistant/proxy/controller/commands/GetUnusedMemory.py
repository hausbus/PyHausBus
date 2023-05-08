import pyhausbus.HausBusUtils as HausBusUtils

class GetUnusedMemory:
  CLASS_ID = 0
  FUNCTION_ID = 4

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetUnusedMemory()

  def __str__(self):
    return f"GetUnusedMemory()"



