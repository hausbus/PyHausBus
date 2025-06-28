from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EState import EState
from pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MEventMask import MEventMask
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.MOptionMask import MOptionMask
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EEnable import EEnable
from pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Enabled import Enabled

class Taster(ABusFeature):
  CLASS_ID:int = 16

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Taster(HausBusUtils.getObjectId(deviceId, 16, instanceId))

  """
  @param state .
  """
  def evClicked(self, state:EState):
    LOGGER.debug("evClicked"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 201, "evClicked")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def evDoubleClick(self, state:EState):
    LOGGER.debug("evDoubleClick"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 202, "evDoubleClick")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def evHoldStart(self, state:EState):
    LOGGER.debug("evHoldStart"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 203, "evHoldStart")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def evHoldEnd(self, state:EState):
    LOGGER.debug("evHoldEnd"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 204, "evHoldEnd")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param holdTimeout Zeit a 10ms.
  @param waitForDoubleClickTimeout Zeit a 10ms.
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  @param debounceTime EntprellZeit in ms 1-254\r\nStandard ist 40ms.
  """
  def setConfiguration(self, holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask, debounceTime:int):
    LOGGER.debug("setConfiguration"+" holdTimeout = "+str(holdTimeout)+" waitForDoubleClickTimeout = "+str(waitForDoubleClickTimeout)+" eventMask = "+str(eventMask)+" optionMask = "+str(optionMask)+" debounceTime = "+str(debounceTime))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(holdTimeout)
    hbCommand.addByte(waitForDoubleClickTimeout)
    hbCommand.addByte(eventMask.getValue())
    hbCommand.addByte(optionMask.getValue())
    hbCommand.addByte(debounceTime)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param holdTimeout Zeit a 10ms.
  @param waitForDoubleClickTimeout Zeit a 10ms.
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  @param debounceTime EntprellZeit in ms 1-254\r\nStandard ist 40ms.
  """
  def Configuration(self, holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask, debounceTime:int):
    LOGGER.debug("Configuration"+" holdTimeout = "+str(holdTimeout)+" waitForDoubleClickTimeout = "+str(waitForDoubleClickTimeout)+" eventMask = "+str(eventMask)+" optionMask = "+str(optionMask)+" debounceTime = "+str(debounceTime))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(holdTimeout)
    hbCommand.addByte(waitForDoubleClickTimeout)
    hbCommand.addByte(eventMask.getValue())
    hbCommand.addByte(optionMask.getValue())
    hbCommand.addByte(debounceTime)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def evCovered(self, state:EState):
    LOGGER.debug("evCovered"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 200, "evCovered")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def evFree(self, state:EState):
    LOGGER.debug("evFree"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 205, "evFree")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param enable FALSE: Deaktiviert das Versenden von Events\r\nTRUE: Aktiviert das Versenden von Events\r\nINVERT: Invertiert das aktuelle Verhalten.
  @param disabledDuration Zeit1s-255s f?  ? ? ?r die die Events deaktiviert werden sollen 0 = unendlich \r\nDieser Parameter wirkt nur.
  """
  def enableEvents(self, enable:EEnable, disabledDuration:int):
    LOGGER.debug("enableEvents"+" enable = "+str(enable)+" disabledDuration = "+str(disabledDuration))
    hbCommand = HausBusCommand(self.objectId, 2, "enableEvents")
    hbCommand.addByte(enable.value)
    hbCommand.addByte(disabledDuration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getStatus(self):
    LOGGER.debug("getStatus")
    hbCommand = HausBusCommand(self.objectId, 3, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param state .
  """
  def Status(self, state:EState):
    LOGGER.debug("Status"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param enabled 0: Events wurden gerade deaktiviert\r\n1: Events wurden gerade aktiviert.
  """
  def evEnabled(self, enabled:int):
    LOGGER.debug("evEnabled"+" enabled = "+str(enabled))
    hbCommand = HausBusCommand(self.objectId, 206, "evEnabled")
    hbCommand.addByte(enabled)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param enabled 0: Events sind deaktviert\r\n1: Events sind aktiviert.
  """
  def Enabled(self, enabled:int):
    LOGGER.debug("Enabled"+" enabled = "+str(enabled))
    hbCommand = HausBusCommand(self.objectId, 130, "Enabled")
    hbCommand.addByte(enabled)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getEnabled(self):
    LOGGER.debug("getEnabled")
    hbCommand = HausBusCommand(self.objectId, 4, "getEnabled")
    ResultWorker()._setResultInfo(Enabled,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def triggerStatusEvent(self):
    LOGGER.debug("triggerStatusEvent")
    hbCommand = HausBusCommand(self.objectId, 5, "triggerStatusEvent")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


