import pyhausbus.HausBusUtils as HausBusUtils

class MinIdleTime:
  CLASS_ID = 176
  FUNCTION_ID = 129

  def __init__(self,time_ms:int):
    self.time_ms=time_ms


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return MinIdleTime(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"MinIdleTime(time_ms={self.time_ms})"

  '''
  @param time_ms Mindestwartezeit [ms].
  '''
  def getTime_ms(self):
    return self.time_ms



