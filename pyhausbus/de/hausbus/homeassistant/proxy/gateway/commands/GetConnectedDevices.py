import pyhausbus.HausBusUtils as HausBusUtils

class GetConnectedDevices:
  CLASS_ID = 176
  FUNCTION_ID = 5

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetConnectedDevices()

  def __str__(self):
    return f"GetConnectedDevices()"



