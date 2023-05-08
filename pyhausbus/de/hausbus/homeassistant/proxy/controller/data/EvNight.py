import pyhausbus.HausBusUtils as HausBusUtils

class EvNight:
  CLASS_ID = 0
  FUNCTION_ID = 207

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvNight()

  def __str__(self):
    return f"EvNight()"



