import pyhausbus.HausBusUtils as HausBusUtils

class GetWeather:
  CLASS_ID = 2
  FUNCTION_ID = 5

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetWeather()

  def __str__(self):
    return f"GetWeather()"



