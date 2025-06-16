from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EState import EState
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 19
  FUNCTION_ID = 129

  def __init__(self,state:EState, duration:int, offTime:int, onTime:int):
    self.state=state
    self.duration=duration
    self.offTime=offTime
    self.onTime=onTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(EState._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Status(state={self.state}, duration={self.duration}, offTime={self.offTime}, onTime={self.onTime})"

  '''
  @param state .
  '''
  def getState(self):
    return self.state

  '''
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos\r\nWenn state TOGGLE.
  '''
  def getDuration(self):
    return self.duration

  '''
  @param offTime Dauer der Aus-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  '''
  def getOffTime(self):
    return self.offTime

  '''
  @param onTime Dauer der An-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  '''
  def getOnTime(self):
    return self.onTime



