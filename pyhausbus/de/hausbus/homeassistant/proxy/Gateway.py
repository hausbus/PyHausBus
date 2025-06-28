from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.MinIdleTime import MinIdleTime
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.ConnectedDevices import ConnectedDevices
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.EValue import EValue

class Gateway(ABusFeature):
  CLASS_ID:int = 176

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Gateway(HausBusUtils.getObjectId(deviceId, 176, instanceId))

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
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param options enabled: Dies Gateway ist aktiv und leitet Nachrichten weiter\r\npreferLoxone: Gateway kommuniziert bevorzugt im Loxone-Protokoll\r\nenableConsole: aktiviert das senden von Debugausgaben\r\nmaster: dieses Gateway soll das Bus-Timing verwalten\r\n\r\nReservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  """
  def setConfiguration(self, options:MOptions):
    LOGGER.debug("setConfiguration"+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(options.getValue())
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getMinIdleTime(self):
    LOGGER.debug("getMinIdleTime")
    hbCommand = HausBusCommand(self.objectId, 3, "getMinIdleTime")
    ResultWorker()._setResultInfo(MinIdleTime,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param time_ms Mindestwartezeit [ms].
  """
  def MinIdleTime(self, time_ms:int):
    LOGGER.debug("MinIdleTime"+" time_ms = "+str(time_ms))
    hbCommand = HausBusCommand(self.objectId, 129, "MinIdleTime")
    hbCommand.addByte(time_ms)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param options enabled: Dies Gateway ist aktiv und leitet Nachrichten weiter\r\npreferLoxone: Gateway kommuniziert bevorzugt im Loxone-Protokoll\r\nenableConsole: aktiviert das senden von Debugausgaben\r\nmaster: dieses Gateway soll das Bus-Timing verwalten.
  """
  def Configuration(self, options:MOptions):
    LOGGER.debug("Configuration"+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(options.getValue())
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param time_ms Mindestwartezeit [ms].
  """
  def setMinIdleTime(self, time_ms:int):
    LOGGER.debug("setMinIdleTime"+" time_ms = "+str(time_ms))
    hbCommand = HausBusCommand(self.objectId, 4, "setMinIdleTime")
    hbCommand.addByte(time_ms)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getConnectedDevices(self):
    LOGGER.debug("getConnectedDevices")
    hbCommand = HausBusCommand(self.objectId, 5, "getConnectedDevices")
    ResultWorker()._setResultInfo(ConnectedDevices,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param deviceIds .
  """
  def ConnectedDevices(self, deviceIds):
    LOGGER.debug("ConnectedDevices"+" deviceIds = "+str(deviceIds))
    hbCommand = HausBusCommand(self.objectId, 130, "ConnectedDevices")
    hbCommand.addMap(deviceIds)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param inMessagesPerMinute Anzahl der eingehenden Nachrichten pro Minute.
  @param outMessagesPerMinute Anzahl der ausgehenden Nachrichten pro Minute.
  @param inBytesPerMinute Anzahl der Datenbytes von eingehenden Nachrichten pro Minute.
  @param outBytesPerMinute Anzahl der Datenbytes von ausgehenden Nachrichten pro Minute.
  @param messageQueueHighWater Maximale Anzahl von Nachrichten in der Warteschlange innerhalb der letzten Minute.
  """
  def evGatewayLoad(self, inMessagesPerMinute:int, outMessagesPerMinute:int, inBytesPerMinute:int, outBytesPerMinute:int, messageQueueHighWater:int):
    LOGGER.debug("evGatewayLoad"+" inMessagesPerMinute = "+str(inMessagesPerMinute)+" outMessagesPerMinute = "+str(outMessagesPerMinute)+" inBytesPerMinute = "+str(inBytesPerMinute)+" outBytesPerMinute = "+str(outBytesPerMinute)+" messageQueueHighWater = "+str(messageQueueHighWater))
    hbCommand = HausBusCommand(self.objectId, 200, "evGatewayLoad")
    hbCommand.addWord(inMessagesPerMinute)
    hbCommand.addWord(outMessagesPerMinute)
    hbCommand.addDWord(inBytesPerMinute)
    hbCommand.addDWord(outBytesPerMinute)
    hbCommand.addByte(messageQueueHighWater)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param value Diese Funktion setzt das Flag \"preferLoxone\" in der Konfiguration entsprechend Persistent..
  """
  def setPreferLoxone(self, value:EValue):
    LOGGER.debug("setPreferLoxone"+" value = "+str(value))
    hbCommand = HausBusCommand(self.objectId, 2, "setPreferLoxone")
    hbCommand.addByte(value.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


