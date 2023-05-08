import pyhausbus.HausBusUtils as HausBusUtils

class Quit:
  CLASS_ID = 1
  FUNCTION_ID = 20

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Quit()

  def __str__(self):
    return f"Quit()"



