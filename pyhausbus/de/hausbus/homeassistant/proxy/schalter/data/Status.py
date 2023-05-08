from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 19
  FUNCTION_ID = 129

  def __init__(self,state:EState, duration:int):
    self.state=state
    self.duration=duration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(EState._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Status(state={self.state}, duration={self.duration})"

  '''
  @param state .
  '''
  def getState(self):
    return self.state

  '''
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  '''
  def getDuration(self):
    return self.duration



