import pyhausbus.HausBusUtils as HausBusUtils

class SetRuleState:
  CLASS_ID = 0
  FUNCTION_ID = 11

  def __init__(self,index:int, state:int):
    self.index=index
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetRuleState(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetRuleState(index={self.index}, state={self.state})"

  '''
  @param index Index des zu setzenden Regelzustandes auf dem Controller..
  '''
  def getIndex(self):
    return self.index

  '''
  @param state Der Zustand wird gesetzt ohne die Aktionen auszufuehren..
  '''
  def getState(self):
    return self.state



