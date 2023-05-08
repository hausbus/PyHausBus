from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class EvFree:
  CLASS_ID = 16
  FUNCTION_ID = 205

  def __init__(self,state:EState):
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvFree(EState._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvFree(state={self.state})"

  '''
  @param state .
  '''
  def getState(self):
    return self.state



