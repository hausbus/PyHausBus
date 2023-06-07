import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.EDirection import EDirection
from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.MOptions import MOptions
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
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param position in Prozent.
  """
  def moveToPosition(self, position:int):
    logging.info("moveToPosition"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 2, "moveToPosition")
    hbCommand.addByte(position)
    hbCommand.send()
    logging.info("returns")

  """
  @param direction .
  """
  def start(self, direction:EDirection):
    logging.info("start"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 3, "start")
    hbCommand.addByte(direction.value)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def stop(self):
    logging.info("stop")
    hbCommand = HausBusCommand(self.objectId, 4, "stop")
    hbCommand.send()
    logging.info("returns")

  """
  @param closeTime Zeit.
  @param openTime Zeit.
  @param options invertDirection: invertiert die Richtung der Ansteuerung des Rollladen.\r\nindependent: behandelt die Relais unabhaengig voneinander d.h. pro Richtung wird nur das jeweilige Relais geschaltet\r\ninvertOutputs: steuert die angeschlossenen Relais mit activLow Logik\r\nenableTracing: Objekt sendet zus?tzliche Events f?r eine Fehlersuche.
  """
  def Configuration(self, closeTime:int, openTime:int, options:MOptions):
    logging.info("Configuration"+" closeTime = "+str(closeTime)+" openTime = "+str(openTime)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(closeTime)
    hbCommand.addByte(openTime)
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param position in Prozent.
  """
  def evClosed(self, position:int):
    logging.info("evClosed"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 200, "evClosed")
    hbCommand.addByte(position)
    hbCommand.send()
    logging.info("returns")

  """
  @param direction .
  """
  def evStart(self, direction:EDirection):
    logging.info("evStart"+" direction = "+str(direction))
    hbCommand = HausBusCommand(self.objectId, 201, "evStart")
    hbCommand.addByte(direction.value)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param position .
  """
  def Status(self, position:int):
    logging.info("Status"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(position)
    hbCommand.send()
    logging.info("returns")

  """
  @param closeTime Zeit.
  @param openTime Zeit.
  @param options invertDirection: invertiert die Richtung der Ansteuerung des Rollladen.\r\nindependent: behandelt die Relais unabhaengig voneinander d.h. pro Richtung wird nur das jeweilige Relais geschaltet\r\ninvertOutputs: steuert die angeschlossenen Relais mit activLow Logik\r\nenableTracing: Objekt sendet zus?tzliche Events f?r eine Fehlersuche.
  """
  def setConfiguration(self, closeTime:int, openTime:int, options:MOptions):
    logging.info("setConfiguration"+" closeTime = "+str(closeTime)+" openTime = "+str(openTime)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(closeTime)
    hbCommand.addByte(openTime)
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param position Aktuelle Position setzen 0-100% geschlossen.
  """
  def setPosition(self, position:int):
    logging.info("setPosition"+" position = "+str(position))
    hbCommand = HausBusCommand(self.objectId, 6, "setPosition")
    hbCommand.addByte(position)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOpen(self):
    logging.info("evOpen")
    hbCommand = HausBusCommand(self.objectId, 202, "evOpen")
    hbCommand.send()
    logging.info("returns")

  """
  @param newState State.
  @param preState State.
  """
  def evNewMainState(self, newState:ENewState, preState:ENewState):
    logging.info("evNewMainState"+" newState = "+str(newState)+" preState = "+str(preState))
    hbCommand = HausBusCommand(self.objectId, 251, "evNewMainState")
    hbCommand.addByte(newState.value)
    hbCommand.addByte(preState.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param newState State.
  @param preState State.
  """
  def evNewSubState(self, newState:ENewState, preState:ENewState):
    logging.info("evNewSubState"+" newState = "+str(newState)+" preState = "+str(preState))
    hbCommand = HausBusCommand(self.objectId, 252, "evNewSubState")
    hbCommand.addByte(newState.value)
    hbCommand.addByte(preState.value)
    hbCommand.send()
    logging.info("returns")


