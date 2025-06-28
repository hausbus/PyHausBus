from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.params.EEnable import EEnable
from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.params.EErrorCode import EErrorCode

class PIDController(ABusFeature):
  CLASS_ID:int = 44

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return PIDController(HausBusUtils.getObjectId(deviceId, 44, instanceId))

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param P P-Anteil des Reglers.
  @param I I-Anteil des Reglers.
  @param D D-Anteil des Reglers.
  @param targetValue Regelungszielwert z.B. targetValue*0.
  @param sensorObjectId Komplette Objekt-ID des Feedback-Sensors.
  @param actorObjectId Komplette Objekt-ID des Stellers.
  @param timeout Zeit.
  @param hysteresis Erweitert den Regelzielwert in einen Bereich\r\n0: Regelzielwert wird versucht exakt zu erreichen\r\n>0: Regelzielwert +/- hysteresis wird versucht zu erreichen.
  @param options additional: erzeugt einen weiteren PIDController.
  """
  def setConfiguration(self, P:int, I:int, D:int, targetValue:int, sensorObjectId:int, actorObjectId:int, timeout:int, hysteresis:int, options:MOptions):
    LOGGER.debug("setConfiguration"+" P = "+str(P)+" I = "+str(I)+" D = "+str(D)+" targetValue = "+str(targetValue)+" sensorObjectId = "+str(sensorObjectId)+" actorObjectId = "+str(actorObjectId)+" timeout = "+str(timeout)+" hysteresis = "+str(hysteresis)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addWord(P)
    hbCommand.addWord(I)
    hbCommand.addWord(D)
    hbCommand.addWord(targetValue)
    hbCommand.addDWord(sensorObjectId)
    hbCommand.addDWord(actorObjectId)
    hbCommand.addWord(timeout)
    hbCommand.addByte(hysteresis)
    hbCommand.addByte(options.getValue())
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param P P-Anteil des Reglers.
  @param I I-Anteil des Reglers.
  @param D D-Anteil des Reglers.
  @param targetValue Regelungszielwert z.B. targetValue*0.
  @param sensorObjectId Komplette Objekt-ID des Feedback-Sensors.
  @param actorObjectId Komplette Objekt-ID des Stellers.
  @param timeout Zeit.
  @param hysteresis Erweitert den Regelzielwert in einen Bereich\r\n0: Regelzielwert wird versucht exakt zu erreichen\r\n>0: Regelzielwert +/- hysteresis wird versucht zu erreichen.
  @param options additional: erzeugt einen weiteren PIDController.
  """
  def Configuration(self, P:int, I:int, D:int, targetValue:int, sensorObjectId:int, actorObjectId:int, timeout:int, hysteresis:int, options:MOptions):
    LOGGER.debug("Configuration"+" P = "+str(P)+" I = "+str(I)+" D = "+str(D)+" targetValue = "+str(targetValue)+" sensorObjectId = "+str(sensorObjectId)+" actorObjectId = "+str(actorObjectId)+" timeout = "+str(timeout)+" hysteresis = "+str(hysteresis)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addWord(P)
    hbCommand.addWord(I)
    hbCommand.addWord(D)
    hbCommand.addWord(targetValue)
    hbCommand.addDWord(sensorObjectId)
    hbCommand.addDWord(actorObjectId)
    hbCommand.addWord(timeout)
    hbCommand.addByte(hysteresis)
    hbCommand.addByte(options.getValue())
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param targetValue Regelungszielwert z.B. targetValue*0.
  """
  def setTargetValue(self, targetValue:int):
    LOGGER.debug("setTargetValue"+" targetValue = "+str(targetValue))
    hbCommand = HausBusCommand(self.objectId, 2, "setTargetValue")
    hbCommand.addWord(targetValue)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param enable Reglerverhalten ein/ausschalten.
  """
  def enable(self, enable:EEnable):
    LOGGER.debug("enable"+" enable = "+str(enable))
    hbCommand = HausBusCommand(self.objectId, 3, "enable")
    hbCommand.addByte(enable.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOn(self):
    LOGGER.debug("evOn")
    hbCommand = HausBusCommand(self.objectId, 200, "evOn")
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
  """
  def evOff(self):
    LOGGER.debug("evOff")
    hbCommand = HausBusCommand(self.objectId, 201, "evOff")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


