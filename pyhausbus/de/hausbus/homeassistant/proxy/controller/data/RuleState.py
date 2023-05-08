import pyhausbus.HausBusUtils as HausBusUtils

class RuleState:
  CLASS_ID = 0
  FUNCTION_ID = 135

  def __init__(self,index:int, state:int):
    self.index=index
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return RuleState(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"RuleState(index={self.index}, state={self.state})"

  '''
  @param index Index der abgefragten Regel.
  '''
  def getIndex(self):
    return self.index

  '''
  @param state Regelzustand.
  '''
  def getState(self):
    return self.state



