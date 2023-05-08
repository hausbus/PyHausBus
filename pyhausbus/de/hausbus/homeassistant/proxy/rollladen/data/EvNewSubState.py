from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.ENewState import ENewState
import pyhausbus.HausBusUtils as HausBusUtils

class EvNewSubState:
  CLASS_ID = 18
  FUNCTION_ID = 252

  def __init__(self,newState:ENewState, preState:ENewState):
    self.newState=newState
    self.preState=preState


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvNewSubState(ENewState._fromBytes(dataIn, offset), ENewState._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvNewSubState(newState={self.newState}, preState={self.preState})"

  '''
  @param newState State.
  '''
  def getNewState(self):
    return self.newState

  '''
  @param preState State.
  '''
  def getPreState(self):
    return self.preState



