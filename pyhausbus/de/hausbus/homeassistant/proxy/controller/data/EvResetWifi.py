import pyhausbus.HausBusUtils as HausBusUtils

class EvResetWifi:
  CLASS_ID = 0
  FUNCTION_ID = 208

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvResetWifi()

  def __str__(self):
    return f"EvResetWifi()"



