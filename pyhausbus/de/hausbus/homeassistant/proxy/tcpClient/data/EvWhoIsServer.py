import pyhausbus.HausBusUtils as HausBusUtils

class EvWhoIsServer:
  CLASS_ID = 91
  FUNCTION_ID = 200

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvWhoIsServer()

  def __str__(self):
    return f"EvWhoIsServer()"



