import pyhausbus.HausBusUtils as HausBusUtils

class GetRuleState:
  CLASS_ID = 0
  FUNCTION_ID = 12

  def __init__(self,index:int):
    self.index=index


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetRuleState(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetRuleState(index={self.index})"

  '''
  @param index Index des abzufragenden Regelzustandes auf dem Controller.
  '''
  def getIndex(self):
    return self.index



