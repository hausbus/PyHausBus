import pyhausbus.HausBusUtils as HausBusUtils

class GetRemoteObjects:
  CLASS_ID = 0
  FUNCTION_ID = 3

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetRemoteObjects()

  def __str__(self):
    return f"GetRemoteObjects()"



