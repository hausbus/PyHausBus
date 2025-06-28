from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.daliLine.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.daliLine.params.EErrorCode import EErrorCode

class DaliLine(ABusFeature):
  CLASS_ID:int = 160

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return DaliLine(HausBusUtils.getObjectId(deviceId, 160, instanceId))

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def getConfiguration(self, address0:int, address1:int, address2:int, address3:int):
    LOGGER.debug("getConfiguration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def setConfiguration(self, address0:int, address1:int, address2:int, address3:int):
    LOGGER.debug("setConfiguration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def allOff(self):
    LOGGER.debug("allOff")
    hbCommand = HausBusCommand(self.objectId, 2, "allOff")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def allOn(self):
    LOGGER.debug("allOn")
    hbCommand = HausBusCommand(self.objectId, 3, "allOn")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param command Dali Kommando s.Spezifikation.
  @param address Kurz- oder Gruppenadresse YAAA AAAS\r\n64 Kurzadressen           0AAA AAAS\r\n16 Gruppenadressen        100A AAAS\r\nSammelaufruf              1111 111S\r\n\r\nY: Adressenart: Y=?  ? ? ??  ?? ??? ??  ?0?  ? ? ??  ?? ??? ??  ? ? Kurzadresse.
  """
  def sendCommand(self, command:int, address:int):
    LOGGER.debug("sendCommand"+" command = "+str(command)+" address = "+str(address))
    hbCommand = HausBusCommand(self.objectId, 4, "sendCommand")
    hbCommand.addByte(command)
    hbCommand.addByte(address)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def Configuration(self, address0:int, address1:int, address2:int, address3:int):
    LOGGER.debug("Configuration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param status .
  """
  def Status(self, status:int):
    LOGGER.debug("Status"+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(status)
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


