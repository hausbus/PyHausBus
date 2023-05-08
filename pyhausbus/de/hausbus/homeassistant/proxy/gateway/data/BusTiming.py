import pyhausbus.HausBusUtils as HausBusUtils

class BusTiming:
  CLASS_ID = 176
  FUNCTION_ID = 129

  def __init__(self,timings):
    self.timings=timings


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return BusTiming(HausBusUtils.bytesToList(dataIn, offset))

  def __str__(self):
    return f"BusTiming(timings={self.timings})"

  '''
  @param timings .
  '''
  def getTimings(self):
    return self.timings



