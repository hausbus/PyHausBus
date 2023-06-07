import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.MOptions import MOptions

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
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
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
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  """
  def setConfiguration(self, options:MOptions):
    logging.info("setConfiguration"+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def checkBusTiming(self):
    logging.info("checkBusTiming")
    hbCommand = HausBusCommand(self.objectId, 2, "checkBusTiming")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getBusTiming(self):
    logging.info("getBusTiming")
    hbCommand = HausBusCommand(self.objectId, 3, "getBusTiming")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param timings .
  """
  def BusTiming(self, timings):
    logging.info("BusTiming"+" timings = "+str(timings))
    hbCommand = HausBusCommand(self.objectId, 129, "BusTiming")
    hbCommand.addMap(timings)
    hbCommand.send()
    logging.info("returns")

  """
  @param options enabled: Dies Gateway ist aktiv und leitet Nachrichten weiter\r\npreferLoxone: Gateway kommuniziert bevorzugt im Loxone-Protokoll.
  """
  def Configuration(self, options:MOptions):
    logging.info("Configuration"+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def resetBusTiming(self):
    logging.info("resetBusTiming")
    hbCommand = HausBusCommand(self.objectId, 4, "resetBusTiming")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getConnectedDevices(self):
    logging.info("getConnectedDevices")
    hbCommand = HausBusCommand(self.objectId, 5, "getConnectedDevices")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param deviceIds .
  """
  def ConnectedDevices(self, deviceIds):
    logging.info("ConnectedDevices"+" deviceIds = "+str(deviceIds))
    hbCommand = HausBusCommand(self.objectId, 130, "ConnectedDevices")
    hbCommand.addMap(deviceIds)
    hbCommand.send()
    logging.info("returns")

  """
  @param messagesPerMinute Anzahl der Nachrichten pro Sekunde.
  @param bytesPerMinute Anzahl der Datenbytes pro Sekunde.
  """
  def evGatewayLoad(self, messagesPerMinute:int, bytesPerMinute:int):
    logging.info("evGatewayLoad"+" messagesPerMinute = "+str(messagesPerMinute)+" bytesPerMinute = "+str(bytesPerMinute))
    hbCommand = HausBusCommand(self.objectId, 200, "evGatewayLoad")
    hbCommand.addWord(messagesPerMinute)
    hbCommand.addDWord(bytesPerMinute)
    hbCommand.send()
    logging.info("returns")


