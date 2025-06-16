import pyhausbus.HausBusUtils as HausBusUtils

class TriggerStatusEvent:
  CLASS_ID = 16
  FUNCTION_ID = 5

  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return TriggerStatusEvent()

  def __str__(self):
    return f"TriggerStatusEvent()"



