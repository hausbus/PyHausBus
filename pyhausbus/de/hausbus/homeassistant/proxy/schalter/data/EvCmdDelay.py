import pyhausbus.HausBusUtils as HausBusUtils

class EvCmdDelay:
  CLASS_ID = 19
  FUNCTION_ID = 203

  def __init__(self,cmdDelay:int):
    self.cmdDelay=cmdDelay


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvCmdDelay(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvCmdDelay(cmdDelay={self.cmdDelay})"

  '''
  @param cmdDelay Dauer Wert * Zeitbasis [ms].
  '''
  def getCmdDelay(self):
    return self.cmdDelay



