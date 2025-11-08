from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.RegisterConfiguration import RegisterConfiguration
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EType import EType
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EFunction import EFunction
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EBaudrate import EBaudrate
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EDataSetting import EDataSetting
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EErrorCode import EErrorCode

class ModBusMaster(ABusFeature):
  CLASS_ID:int = 45

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return ModBusMaster(HausBusUtils.getObjectId(deviceId, 45, instanceId))

  """
  @param idx index of the configuration slot.
  """
  def getRegisterConfiguration(self, idx:int):
    LOGGER.debug("getRegisterConfiguration"+" idx = "+str(idx))
    hbCommand = HausBusCommand(self.objectId, 2, "getRegisterConfiguration")
    hbCommand.addByte(idx)
    ResultWorker()._setResultInfo(RegisterConfiguration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param idx index of the configuration slot.
  @param node Geraeteadresse im ModBus.
  @param type Unterstuetzte Register Typen.
  @param address Register Adresse.
  """
  def setRegisterConfiguration(self, idx:int, node:int, type:EType, address:int):
    LOGGER.debug("setRegisterConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" type = "+str(type)+" address = "+str(address))
    hbCommand = HausBusCommand(self.objectId, 3, "setRegisterConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(type.value)
    hbCommand.addWord(address)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param idx index of the configuration slot.
  @param node device node on ModBus.
  @param type Unterstuetzte Register Typen.
  @param address Register Adresse.
  """
  def RegisterConfiguration(self, idx:int, node:int, type:EType, address:int):
    LOGGER.debug("RegisterConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" type = "+str(type)+" address = "+str(address))
    hbCommand = HausBusCommand(self.objectId, 129, "RegisterConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(type.value)
    hbCommand.addWord(address)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param node Bus-Knoten Geraete-Adresse.
  @param function Mod-Bus Funktion.
  @param address Adresse in Geraet.
  @param data Daten.
  """
  def genericResponse(self, node:int, function:EFunction, address:int, data:bytearray):
    LOGGER.debug("genericResponse"+" node = "+str(node)+" function = "+str(function)+" address = "+str(address)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 130, "genericResponse")
    hbCommand.addByte(node)
    hbCommand.addByte(function.value)
    hbCommand.addWord(address)
    hbCommand.addBlob(data)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param node Bus-Knoten Geraete-Adresse.
  @param function Mod-Bus Funktion.
  @param address Adresse in Geraet.
  @param data Daten.
  """
  def genericCommand(self, node:int, function:EFunction, address:int, data:bytearray):
    LOGGER.debug("genericCommand"+" node = "+str(node)+" function = "+str(function)+" address = "+str(address)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 4, "genericCommand")
    hbCommand.addByte(node)
    hbCommand.addByte(function.value)
    hbCommand.addWord(address)
    hbCommand.addBlob(data)
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
  @param baudrate Verbindungsgeschwindigkeit.
  @param dataSetting Anzahl Daten-Bits.
  @param responseTimeout Zeit in [ms] um auf eine Antwort zu warten.
  """
  def setConfiguration(self, baudrate:EBaudrate, dataSetting:EDataSetting, responseTimeout:int):
    LOGGER.debug("setConfiguration"+" baudrate = "+str(baudrate)+" dataSetting = "+str(dataSetting)+" responseTimeout = "+str(responseTimeout))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(baudrate.value)
    hbCommand.addByte(dataSetting.value)
    hbCommand.addWord(responseTimeout)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param baudrate Verbindungsgeschwindigkeit.
  @param dataSetting Anzahl Daten-Bits.
  @param responseTimeout Zeit in [ms] um auf eine Antwort zu warten.
  """
  def Configuration(self, baudrate:EBaudrate, dataSetting:EDataSetting, responseTimeout:int):
    LOGGER.debug("Configuration"+" baudrate = "+str(baudrate)+" dataSetting = "+str(dataSetting)+" responseTimeout = "+str(responseTimeout))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(baudrate.value)
    hbCommand.addByte(dataSetting.value)
    hbCommand.addWord(responseTimeout)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode .
  @param data .
  """
  def evError(self, errorCode:EErrorCode, data:int):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    hbCommand.addByte(data)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


