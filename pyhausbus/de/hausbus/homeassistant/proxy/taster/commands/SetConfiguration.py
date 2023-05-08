from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MEventMask import MEventMask
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MOptionMask import MOptionMask
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 16
  FUNCTION_ID = 1

  def __init__(self,holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask, debounceTime:int):
    self.holdTimeout=holdTimeout
    self.waitForDoubleClickTimeout=waitForDoubleClickTimeout
    self.eventMask=eventMask
    self.optionMask=optionMask
    self.debounceTime=debounceTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), MEventMask._fromBytes(dataIn, offset), MOptionMask._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(holdTimeout={self.holdTimeout}, waitForDoubleClickTimeout={self.waitForDoubleClickTimeout}, eventMask={self.eventMask}, optionMask={self.optionMask}, debounceTime={self.debounceTime})"

  '''
  @param holdTimeout Zeit a 10ms.
  '''
  def getHoldTimeout(self):
    return self.holdTimeout

  '''
  @param waitForDoubleClickTimeout Zeit a 10ms.
  '''
  def getWaitForDoubleClickTimeout(self):
    return self.waitForDoubleClickTimeout

  '''
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  '''
  def getEventMask(self) -> MEventMask:
    return self.eventMask

  '''
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  '''
  def getOptionMask(self) -> MOptionMask:
    return self.optionMask

  '''
  @param debounceTime EntprellZeit in ms 1-254\r\nStandard ist 40ms.
  '''
  def getDebounceTime(self):
    return self.debounceTime



