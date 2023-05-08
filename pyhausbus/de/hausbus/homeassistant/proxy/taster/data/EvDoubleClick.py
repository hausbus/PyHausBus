from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class EvDoubleClick:
  CLASS_ID = 16
  FUNCTION_ID = 202

  def __init__(self,state:EState):
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDoubleClick(EState._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvDoubleClick(state={self.state})"

  '''
  @param state .
  '''
  def getState(self):
    return self.state



