from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class EvCovered:
  CLASS_ID = 16
  FUNCTION_ID = 200

  def __init__(self,state:EState):
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvCovered(EState._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvCovered(state={self.state})"

  '''
  @param state .
  '''
  def getState(self):
    return self.state



