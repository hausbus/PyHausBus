from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.MEventMask import MEventMask
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.MOptionMask import MOptionMask
import pyhausbus.HausBusUtils as HausBusUtils

class SetButtonConfiguration:
  CLASS_ID = 20
  FUNCTION_ID = 11

  def __init__(self,holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask):
    self.holdTimeout=holdTimeout
    self.waitForDoubleClickTimeout=waitForDoubleClickTimeout
    self.eventMask=eventMask
    self.optionMask=optionMask


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetButtonConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), MEventMask._fromBytes(dataIn, offset), MOptionMask._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetButtonConfiguration(holdTimeout={self.holdTimeout}, waitForDoubleClickTimeout={self.waitForDoubleClickTimeout}, eventMask={self.eventMask}, optionMask={self.optionMask})"

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



