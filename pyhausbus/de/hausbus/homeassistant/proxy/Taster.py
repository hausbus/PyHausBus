import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EState import EState
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MEventMask import MEventMask
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MOptionMask import MOptionMask
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EEnable import EEnable

class Taster(ABusFeature):
  CLASS_ID:int = 16

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  @param state .
  """
  def evClicked(self, state:EState):
    logging.info("evClicked"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 201, "evClicked")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param state .
  """
  def evDoubleClick(self, state:EState):
    logging.info("evDoubleClick"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 202, "evDoubleClick")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param state .
  """
  def evHoldStart(self, state:EState):
    logging.info("evHoldStart"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 203, "evHoldStart")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param state .
  """
  def evHoldEnd(self, state:EState):
    logging.info("evHoldEnd"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 204, "evHoldEnd")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param holdTimeout Zeit a 10ms.
  @param waitForDoubleClickTimeout Zeit a 10ms.
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  @param debounceTime EntprellZeit in ms 1-254\r\nStandard ist 40ms.
  """
  def setConfiguration(self, holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask, debounceTime:int):
    logging.info("setConfiguration"+" holdTimeout = "+str(holdTimeout)+" waitForDoubleClickTimeout = "+str(waitForDoubleClickTimeout)+" eventMask = "+str(eventMask)+" optionMask = "+str(optionMask)+" debounceTime = "+str(debounceTime))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(holdTimeout)
    hbCommand.addByte(waitForDoubleClickTimeout)
    hbCommand.addByte(eventMask.getValue())
    hbCommand.addByte(optionMask.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.send()
    logging.info("returns")

  """
  @param holdTimeout Zeit a 10ms.
  @param waitForDoubleClickTimeout Zeit a 10ms.
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  @param debounceTime EntprellZeit in ms 1-254\r\nStandard ist 40ms.
  """
  def Configuration(self, holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask, debounceTime:int):
    logging.info("Configuration"+" holdTimeout = "+str(holdTimeout)+" waitForDoubleClickTimeout = "+str(waitForDoubleClickTimeout)+" eventMask = "+str(eventMask)+" optionMask = "+str(optionMask)+" debounceTime = "+str(debounceTime))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(holdTimeout)
    hbCommand.addByte(waitForDoubleClickTimeout)
    hbCommand.addByte(eventMask.getValue())
    hbCommand.addByte(optionMask.getValue())
    hbCommand.addByte(debounceTime)
    hbCommand.send()
    logging.info("returns")

  """
  @param state .
  """
  def evCovered(self, state:EState):
    logging.info("evCovered"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 200, "evCovered")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param state .
  """
  def evFree(self, state:EState):
    logging.info("evFree"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 205, "evFree")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:int):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode)
    hbCommand.send()
    logging.info("returns")

  """
  @param enable FALSE: Deaktiviert das Versenden von Events\r\nTRUE: Aktiviert das Versenden von Events\r\nINVERT: Invertiert das aktuelle Verhalten.
  @param disabledDuration Zeit1s-255s f?  ? ? ?r die die Events deaktiviert werden sollen 0 = unendlich \r\nDieser Parameter wirkt nur.
  """
  def enableEvents(self, enable:EEnable, disabledDuration:int):
    logging.info("enableEvents"+" enable = "+str(enable)+" disabledDuration = "+str(disabledDuration))
    hbCommand = HausBusCommand(self.objectId, 2, "enableEvents")
    hbCommand.addByte(enable.value)
    hbCommand.addByte(disabledDuration)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 3, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param state .
  """
  def Status(self, state:EState):
    logging.info("Status"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param enabled 0: Events wurden gerade deaktiviert\r\n1: Events wurden gerade aktiviert.
  """
  def evEnabled(self, enabled:int):
    logging.info("evEnabled"+" enabled = "+str(enabled))
    hbCommand = HausBusCommand(self.objectId, 206, "evEnabled")
    hbCommand.addByte(enabled)
    hbCommand.send()
    logging.info("returns")

  """
  @param enabled 0: Events sind deaktviert\r\n1: Events sind aktiviert.
  """
  def Enabled(self, enabled:int):
    logging.info("Enabled"+" enabled = "+str(enabled))
    hbCommand = HausBusCommand(self.objectId, 130, "Enabled")
    hbCommand.addByte(enabled)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getEnabled(self):
    logging.info("getEnabled")
    hbCommand = HausBusCommand(self.objectId, 4, "getEnabled")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject


