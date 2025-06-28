from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.EDirection import EDirection
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.ENewState import ENewState

class Rollladen(ABusFeature):
  CLASS_ID:int = 18

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Rollladen(HausBusUtils.getObjectId(deviceId, 18, instanceId))

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param position in Prozent.
  """
  def moveToPosition(self, position:int):
    LOGGER.debug("moveToPosition"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 2, "moveToPosition")
    hbCommand.addByte(position)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param direction .
  """
  def start(self, direction:EDirection):
    LOGGER.debug("start"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 3, "start")
    hbCommand.addByte(direction.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def stop(self):
    LOGGER.debug("stop")
    hbCommand = HausBusCommand(self.objectId, 4, "stop")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param closeTime Zeit.
  @param openTime Zeit.
  @param options invertDirection: invertiert die Richtung der Ansteuerung des Rollladen.\r\nindependent: behandelt die Relais unabhaengig voneinander d.h. pro Richtung wird nur das jeweilige Relais geschaltet\r\ninvertOutputs: steuert die angeschlossenen Relais mit activLow Logik\r\nenableTracing: Objekt sendet zus?tzliche Events f?r eine Fehlersuche.
  """
  def Configuration(self, closeTime:int, openTime:int, options:MOptions):
    LOGGER.debug("Configuration"+" closeTime = "+str(closeTime)+" openTime = "+str(openTime)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(closeTime)
    hbCommand.addByte(openTime)
    hbCommand.addByte(options.getValue())
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param position in Prozent.
  """
  def evClosed(self, position:int):
    LOGGER.debug("evClosed"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 200, "evClosed")
    hbCommand.addByte(position)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param direction .
  """
  def evStart(self, direction:EDirection):
    LOGGER.debug("evStart"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 201, "evStart")
    hbCommand.addByte(direction.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getStatus(self):
    LOGGER.debug("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param position .
  """
  def Status(self, position:int):
    LOGGER.debug("Status"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(position)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param closeTime Zeit.
  @param openTime Zeit.
  @param options invertDirection: invertiert die Richtung der Ansteuerung des Rollladen.\r\nindependent: behandelt die Relais unabhaengig voneinander d.h. pro Richtung wird nur das jeweilige Relais geschaltet\r\ninvertOutputs: steuert die angeschlossenen Relais mit activLow Logik\r\nenableTracing: Objekt sendet zus?tzliche Events f?r eine Fehlersuche.
  """
  def setConfiguration(self, closeTime:int, openTime:int, options:MOptions):
    LOGGER.debug("setConfiguration"+" closeTime = "+str(closeTime)+" openTime = "+str(openTime)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(closeTime)
    hbCommand.addByte(openTime)
    hbCommand.addByte(options.getValue())
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
  @param position Aktuelle Position setzen 0-100% geschlossen.
  """
  def setPosition(self, position:int):
    LOGGER.debug("setPosition"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 6, "setPosition")
    hbCommand.addByte(position)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOpen(self):
    LOGGER.debug("evOpen")
    hbCommand = HausBusCommand(self.objectId, 202, "evOpen")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param newState State.
  @param preState State.
  """
  def evNewMainState(self, newState:ENewState, preState:ENewState):
    LOGGER.debug("evNewMainState"+" newState = "+str(newState)+" preState = "+str(preState))
    hbCommand = HausBusCommand(self.objectId, 251, "evNewMainState")
    hbCommand.addByte(newState.value)
    hbCommand.addByte(preState.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param newState State.
  @param preState State.
  """
  def evNewSubState(self, newState:ENewState, preState:ENewState):
    LOGGER.debug("evNewSubState"+" newState = "+str(newState)+" preState = "+str(preState))
    hbCommand = HausBusCommand(self.objectId, 252, "evNewSubState")
    hbCommand.addByte(newState.value)
    hbCommand.addByte(preState.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


