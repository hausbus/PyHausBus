from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class State:
  CLASS_ID = 43
  FUNCTION_ID = 129

  def __init__(self,state:EState):
    self.state=state


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return State(EState._fromBytes(dataIn, offset))

  def __str__(self):
    return f"State(state={self.state})"

  '''
  @param state State of the RFID-Reader hardware.
  '''
  def getState(self):
    return self.state



