from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EState import EState
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.Configuration import Configuration

class Schalter(ABusFeature):
  CLASS_ID:int = 19

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Schalter(HausBusUtils.getObjectId(deviceId, 19, instanceId))

  """
  @param offTime Ausschaltdauer: \r\nWert * Zeitbasis [ms].
  @param onTime Einschaltdauer: \r\nWert * Zeitbasis [ms].
  @param quantity Anzahl der Zustandswechsel.
  """
  def toggle(self, offTime:int, onTime:int, quantity:int):
    LOGGER.debug("toggle"+" offTime = "+str(offTime)+" onTime = "+str(onTime)+" quantity = "+str(quantity))
    hbCommand = HausBusCommand(self.objectId, 4, "toggle")
    hbCommand.addByte(offTime)
    hbCommand.addByte(onTime)
    hbCommand.addByte(quantity)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param duration Einschaltdauer: \r\nWert * Zeitbasis [ms]\r\n0=nicht mehr ausschalten.
  @param onDelay Einschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def on(self, duration:int, onDelay:int):
    LOGGER.debug("on"+" duration = "+str(duration)+" onDelay = "+str(onDelay))
    hbCommand = HausBusCommand(self.objectId, 3, "on")
    hbCommand.addWord(duration)
    hbCommand.addWord(onDelay)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def off(self, offDelay:int):
    LOGGER.debug("off"+" offDelay = "+str(offDelay))
    hbCommand = HausBusCommand(self.objectId, 2, "off")
    hbCommand.addWord(offDelay)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param duration Dauer.
  """
  def evOn(self, duration:int):
    LOGGER.debug("evOn"+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addWord(duration)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOff(self):
    LOGGER.debug("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
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
  @param state .
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos\r\nWenn state TOGGLE.
  @param offTime Dauer der Aus-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  @param onTime Dauer der An-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  """
  def Status(self, state:EState, duration:int, offTime:int, onTime:int):
    LOGGER.debug("Status"+" state = "+str(state)+" duration = "+str(duration)+" offTime = "+str(offTime)+" onTime = "+str(onTime))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(state.value)
    hbCommand.addWord(duration)
    hbCommand.addByte(offTime)
    hbCommand.addByte(onTime)
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
  @param offTime Dauer der Aus-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  @param onTime Dauer der An-Phase beim Togglen: \r\nWert * Zeitbasis [ms].
  @param quantity Anzahl der Schaltvorgaenge.
  """
  def evToggle(self, offTime:int, onTime:int, quantity:int):
    LOGGER.debug("evToggle"+" offTime = "+str(offTime)+" onTime = "+str(onTime)+" quantity = "+str(quantity))
    hbCommand = HausBusCommand(self.objectId, 202, "evToggle")
    hbCommand.addByte(offTime)
    hbCommand.addByte(onTime)
    hbCommand.addByte(quantity)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param maxOnTime Maximale Zeit.
  @param offDelayTime Verzoegerungszeit nach einem Off-Kommando.
  @param timeBase Zeitbasis [ms] fuer die Zeitabhaengigen Befehle.
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  @param disableBitIndex Bit Index0-31 Systemvariable.
  """
  def Configuration(self, maxOnTime:int, offDelayTime:int, timeBase:int, options:MOptions, disableBitIndex:int):
    LOGGER.debug("Configuration"+" maxOnTime = "+str(maxOnTime)+" offDelayTime = "+str(offDelayTime)+" timeBase = "+str(timeBase)+" options = "+str(options)+" disableBitIndex = "+str(disableBitIndex))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(maxOnTime)
    hbCommand.addByte(offDelayTime)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.addByte(disableBitIndex)
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
  @param maxOnTime Maximale Zeit.
  @param offDelayTime Verzoegerungszeit nach einem Off-Kommando.
  @param timeBase Zeitbasis [ms] fuer die Zeitabhaengigen Befehle.
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  @param disableBitIndex Bit Index0-31 Systemvariable.
  """
  def setConfiguration(self, maxOnTime:int, offDelayTime:int, timeBase:int, options:MOptions, disableBitIndex:int):
    LOGGER.debug("setConfiguration"+" maxOnTime = "+str(maxOnTime)+" offDelayTime = "+str(offDelayTime)+" timeBase = "+str(timeBase)+" options = "+str(options)+" disableBitIndex = "+str(disableBitIndex))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(maxOnTime)
    hbCommand.addByte(offDelayTime)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.addByte(disableBitIndex)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param cmdDelay Dauer Wert * Zeitbasis [ms].
  """
  def evCmdDelay(self, cmdDelay:int):
    LOGGER.debug("evCmdDelay"+" cmdDelay = "+str(cmdDelay))
    hbCommand = HausBusCommand(self.objectId, 203, "evCmdDelay")
    hbCommand.addWord(cmdDelay)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evDisabled(self):
    LOGGER.debug("evDisabled")
    hbCommand = HausBusCommand(self.objectId, 204, "evDisabled")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param duty 0-100% Pulsverh?ltnis.
  @param quantity Anzahl der Zustandswechsel.
  """
  def toggleByDuty(self, duty:int, quantity:int):
    LOGGER.debug("toggleByDuty"+" duty = "+str(duty)+" quantity = "+str(quantity))
    hbCommand = HausBusCommand(self.objectId, 6, "toggleByDuty")
    hbCommand.addByte(duty)
    hbCommand.addByte(quantity)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param duty 0-100% Pulsverh?ltnis.
  @param durationSeconds Einschaltdauer in Sekunden.
  """
  def evToggleByDuty(self, duty:int, durationSeconds:int):
    LOGGER.debug("evToggleByDuty"+" duty = "+str(duty)+" durationSeconds = "+str(durationSeconds))
    hbCommand = HausBusCommand(self.objectId, 205, "evToggleByDuty")
    hbCommand.addByte(duty)
    hbCommand.addWord(durationSeconds)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


