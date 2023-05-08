import pyhausbus.HausBusUtils as HausBusUtils

class Off:
  CLASS_ID = 21
  FUNCTION_ID = 2

  def __init__(self,offDelay:int):
    self.offDelay=offDelay


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Off(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Off(offDelay={self.offDelay})"

  '''
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  '''
  def getOffDelay(self):
    return self.offDelay



