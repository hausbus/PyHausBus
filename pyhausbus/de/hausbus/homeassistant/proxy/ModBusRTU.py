from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.data.RegisterConfiguration import RegisterConfiguration
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ERegisterType import ERegisterType
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ESensorType import ESensorType
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ESiPrefix import ESiPrefix
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.EFunction import EFunction
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.EBaudrate import EBaudrate
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.EDataSetting import EDataSetting
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.EErrorCode import EErrorCode

class ModBusRTU(ABusFeature):
  CLASS_ID:int = 45

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return ModBusRTU(HausBusUtils.getObjectId(deviceId, 45, instanceId))

  """
  @param idx index of the configuration slot.
  """
  def getRegisterConfiguration(self, idx:int):
    LOGGER.debug("getRegisterConfiguration"+" idx = "+str(idx))
    hbCommand = HausBusCommand(self.objectId, 2, "getRegisterConfiguration")
    hbCommand.addByte(idx)
    ResultWorker()._setResultInfo(RegisterConfiguration,self.getObjectId())
    hbCommand.send()


  """
  @param idx index of the configuration slot.
  @param node Geraeteadresse im ModBus.
  @param registerType Unterstuetzte Register Typen.
  @param address Register Adresse.
  @param sensorType Sensor Typ meldet sich dann mit der entsprechenden Feature-Klasse.
  @param siPrefix Si-Prefix f?r den Zahlenwert im ModBus-Register.
  """
  def setRegisterConfiguration(self, idx:int, node:int, registerType:ERegisterType, address:int, sensorType:ESensorType, siPrefix:ESiPrefix):
    LOGGER.debug("setRegisterConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" registerType = "+str(registerType)+" address = "+str(address)+" sensorType = "+str(sensorType)+" siPrefix = "+str(siPrefix))
    hbCommand = HausBusCommand(self.objectId, 3, "setRegisterConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(registerType.value)
    hbCommand.addWord(address)
    hbCommand.addByte(sensorType.value)
    hbCommand.addByte(siPrefix.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param idx index der Konfiguration.
  @param node Knoten Nummer im BUS.
  @param registerType Unterstuetzte Register Typen.
  @param address Register Adresse.
  @param sensorType Sensor Typ meldet sich dann mit der entsprechenden Feature-Klasse.
  @param siPrefix Si-Prefix f?r den Zahlenwert im ModBus-Register.
  """
  def RegisterConfiguration(self, idx:int, node:int, registerType:ERegisterType, address:int, sensorType:ESensorType, siPrefix:ESiPrefix):
    LOGGER.debug("RegisterConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" registerType = "+str(registerType)+" address = "+str(address)+" sensorType = "+str(sensorType)+" siPrefix = "+str(siPrefix))
    hbCommand = HausBusCommand(self.objectId, 129, "RegisterConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(registerType.value)
    hbCommand.addWord(address)
    hbCommand.addByte(sensorType.value)
    hbCommand.addByte(siPrefix.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param node Bus-Knoten Geraete-Adresse.
  @param function Mod-Bus Funktion.
  @param data Daten.
  """
  def Response(self, node:int, function:EFunction, data:bytearray):
    LOGGER.debug("Response"+" node = "+str(node)+" function = "+str(function)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 130, "Response")
    hbCommand.addByte(node)
    hbCommand.addByte(function.value)
    hbCommand.addBlob(data)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param node Bus-Knoten Geraete-Adresse.
  @param function Mod-Bus Funktion.
  @param address Adresse in Geraet.
  @param data Daten.
  """
  def sendRequest(self, node:int, function:EFunction, address:int, data:bytearray):
    LOGGER.debug("sendRequest"+" node = "+str(node)+" function = "+str(function)+" address = "+str(address)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 4, "sendRequest")
    hbCommand.addByte(node)
    hbCommand.addByte(function.value)
    hbCommand.addWord(address)
    hbCommand.addBlob(data)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()


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



