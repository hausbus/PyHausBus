import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 43
  FUNCTION_ID = 128

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration()

  def __str__(self):
    return f"Configuration()"



