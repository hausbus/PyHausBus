import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import EFirmwareId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MLogicalButtonMask import MLogicalButtonMask
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.ESlotType import ESlotType
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EStatus import EStatus
from pyhausbus.WeekTime import WeekTime
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EReason import EReason
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MOption import MOption
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EType import EType
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFeatureId import EFeatureId

class Controller(ABusFeature):
  CLASS_ID:int = 0

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Controller(HausBusUtils.getObjectId(deviceId, 0, instanceId))

  """
  @param index .
  """
  def getModuleId(self, index:EIndex):
    logging.info("getModuleId"+" index = "+str(index))
    hbCommand = HausBusCommand(self.objectId, 2, "getModuleId")
    hbCommand.addByte(index.value)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  """
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 5, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param name Modulname.
  @param size Modulgroesse in Bytes.
  @param majorRelease Release-Kennung Format major.minor.
  @param minorRelease Release-Kennung Format major.minor.
  @param firmwareId Firmware-Kennung.
  """
  def ModuleId(self, name:str, size:int, majorRelease:int, minorRelease:int, firmwareId:EFirmwareId):
    logging.info("ModuleId"+" name = "+str(name)+" size = "+str(size)+" majorRelease = "+str(majorRelease)+" minorRelease = "+str(minorRelease)+" firmwareId = "+str(firmwareId))
    hbCommand = HausBusCommand(self.objectId, 128, "ModuleId")
    hbCommand.addString(name)
    hbCommand.addDWord(size)
    hbCommand.addByte(majorRelease)
    hbCommand.addByte(minorRelease)
    hbCommand.addByte(firmwareId.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param startupDelay a 250ms.
  @param logicalButtonMask jedes Bit enspricht einem logischem Taster.
  @param deviceId .
  @param reportMemoryStatusTime Zeitinterval in Minuten1-255min.
  @param slotType0 .
  @param slotType1 .
  @param slotType2 .
  @param slotType3 .
  @param slotType4 .
  @param slotType5 .
  @param slotType6 .
  @param slotType7 .
  @param timeCorrection Korregiert den internen Zeitgeber um diesen Wert pro Minute.
  @param reserve .
  @param dataBlockSize maximale Groesse des Datenblocks in einer Nachricht.
  @param FCKE ControllerBoard Version Bsp. 30 = v3.0.
  """
  def Configuration(self, startupDelay:int, logicalButtonMask:MLogicalButtonMask, deviceId:int, reportMemoryStatusTime:int, slotType0:ESlotType, slotType1:ESlotType, slotType2:ESlotType, slotType3:ESlotType, slotType4:ESlotType, slotType5:ESlotType, slotType6:ESlotType, slotType7:ESlotType, timeCorrection:int, reserve:int, dataBlockSize:int, FCKE:int):
    logging.info("Configuration"+" startupDelay = "+str(startupDelay)+" logicalButtonMask = "+str(logicalButtonMask)+" deviceId = "+str(deviceId)+" reportMemoryStatusTime = "+str(reportMemoryStatusTime)+" slotType0 = "+str(slotType0)+" slotType1 = "+str(slotType1)+" slotType2 = "+str(slotType2)+" slotType3 = "+str(slotType3)+" slotType4 = "+str(slotType4)+" slotType5 = "+str(slotType5)+" slotType6 = "+str(slotType6)+" slotType7 = "+str(slotType7)+" timeCorrection = "+str(timeCorrection)+" reserve = "+str(reserve)+" dataBlockSize = "+str(dataBlockSize)+" FCKE = "+str(FCKE))
    hbCommand = HausBusCommand(self.objectId, 131, "Configuration")
    hbCommand.addByte(startupDelay)
    hbCommand.addByte(logicalButtonMask.getValue())
    hbCommand.addWord(deviceId)
    hbCommand.addByte(reportMemoryStatusTime)
    hbCommand.addByte(slotType0.value)
    hbCommand.addByte(slotType1.value)
    hbCommand.addByte(slotType2.value)
    hbCommand.addByte(slotType3.value)
    hbCommand.addByte(slotType4.value)
    hbCommand.addByte(slotType5.value)
    hbCommand.addByte(slotType6.value)
    hbCommand.addByte(slotType7.value)
    hbCommand.addByte(timeCorrection)
    hbCommand.addWord(reserve)
    hbCommand.addWord(dataBlockSize)
    hbCommand.addByte(FCKE)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getRemoteObjects(self):
    logging.info("getRemoteObjects")
    hbCommand = HausBusCommand(self.objectId, 3, "getRemoteObjects")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param objectList Eine Liste der Verfuegbaren Objekte im Geraete.
  """
  def RemoteObjects(self, objectList):
    logging.info("RemoteObjects"+" objectList = "+str(objectList))
    hbCommand = HausBusCommand(self.objectId, 129, "RemoteObjects")
    hbCommand.addMap(objectList)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def generateRandomDeviceId(self):
    logging.info("generateRandomDeviceId")
    hbCommand = HausBusCommand(self.objectId, 0, "generateRandomDeviceId")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def reset(self):
    logging.info("reset")
    hbCommand = HausBusCommand(self.objectId, 1, "reset")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getUnusedMemory(self):
    logging.info("getUnusedMemory")
    hbCommand = HausBusCommand(self.objectId, 4, "getUnusedMemory")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param startupDelay a 10ms.
  @param logicalButtonMask jedes Bit enspricht einem logischem Taster.
  @param deviceId .
  @param reportMemoryStatusTime Zeitinterval in Minuten1-255min.
  @param slotType0 .
  @param slotType1 .
  @param slotType2 .
  @param slotType3 .
  @param slotType4 .
  @param slotType5 .
  @param slotType6 .
  @param slotType7 .
  """
  def setConfiguration(self, startupDelay:int, logicalButtonMask:MLogicalButtonMask, deviceId:int, reportMemoryStatusTime:int, slotType0:ESlotType, slotType1:ESlotType, slotType2:ESlotType, slotType3:ESlotType, slotType4:ESlotType, slotType5:ESlotType, slotType6:ESlotType, slotType7:ESlotType):
    logging.info("setConfiguration"+" startupDelay = "+str(startupDelay)+" logicalButtonMask = "+str(logicalButtonMask)+" deviceId = "+str(deviceId)+" reportMemoryStatusTime = "+str(reportMemoryStatusTime)+" slotType0 = "+str(slotType0)+" slotType1 = "+str(slotType1)+" slotType2 = "+str(slotType2)+" slotType3 = "+str(slotType3)+" slotType4 = "+str(slotType4)+" slotType5 = "+str(slotType5)+" slotType6 = "+str(slotType6)+" slotType7 = "+str(slotType7))
    hbCommand = HausBusCommand(self.objectId, 6, "setConfiguration")
    hbCommand.addByte(startupDelay)
    hbCommand.addByte(logicalButtonMask.getValue())
    hbCommand.addWord(deviceId)
    hbCommand.addByte(reportMemoryStatusTime)
    hbCommand.addByte(slotType0.value)
    hbCommand.addByte(slotType1.value)
    hbCommand.addByte(slotType2.value)
    hbCommand.addByte(slotType3.value)
    hbCommand.addByte(slotType4.value)
    hbCommand.addByte(slotType5.value)
    hbCommand.addByte(slotType6.value)
    hbCommand.addByte(slotType7.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param freeStack Anzahl des nicht genutzten Stacks in Bytes..
  @param freeHeap Aktuell freier Heap in Bytes..
  """
  def UnusedMemory(self, freeStack:int, freeHeap:int):
    logging.info("UnusedMemory"+" freeStack = "+str(freeStack)+" freeHeap = "+str(freeHeap))
    hbCommand = HausBusCommand(self.objectId, 130, "UnusedMemory")
    hbCommand.addWord(freeStack)
    hbCommand.addWord(freeHeap)
    hbCommand.send()
    logging.info("returns")

  """
  @param address .
  @param length .
  """
  def readMemory(self, address:int, length:int):
    logging.info("readMemory"+" address = "+str(address)+" length = "+str(length))
    hbCommand = HausBusCommand(self.objectId, 7, "readMemory")
    hbCommand.addDWord(address)
    hbCommand.addWord(length)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param address .
  @param data .
  """
  def writeMemory(self, address:int, data:bytearray):
    logging.info("writeMemory"+" address = "+str(address)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 8, "writeMemory")
    hbCommand.addDWord(address)
    hbCommand.addBlob(data)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  """
  def ping(self):
    logging.info("ping")
    hbCommand = HausBusCommand(self.objectId, 127, "ping")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  """
  def pong(self):
    logging.info("pong")
    hbCommand = HausBusCommand(self.objectId, 199, "pong")
    hbCommand.send()
    logging.info("returns")

  """
  @param address Adresse des gemeldeten Speicherinhaltes.
  @param data Daten....
  """
  def MemoryData(self, address:int, data:bytearray):
    logging.info("MemoryData"+" address = "+str(address)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 132, "MemoryData")
    hbCommand.addDWord(address)
    hbCommand.addBlob(data)
    hbCommand.send()
    logging.info("returns")

  """
  @param status Status des letzten Speicherzugriffs.
  @param address Speicheradresse zu dem dieser Status gesendet wird..
  """
  def MemoryStatus(self, status:EStatus, address:int):
    logging.info("MemoryStatus"+" status = "+str(status)+" address = "+str(address))
    hbCommand = HausBusCommand(self.objectId, 133, "MemoryStatus")
    hbCommand.addByte(status.value)
    hbCommand.addDWord(address)
    hbCommand.send()
    logging.info("returns")

  """
  @param offset aktueller Offset im Gesamtregelblock.
  @param data .
  """
  def writeRules(self, offset:int, data:bytearray):
    logging.info("writeRules"+" offset = "+str(offset)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 9, "writeRules")
    hbCommand.addWord(offset)
    hbCommand.addBlob(data)
    hbCommand.send()
    logging.info("returns")

  """
  @param offset Offset im Gesamtregelblock.
  @param length Datenlaenge.
  """
  def readRules(self, offset:int, length:int):
    logging.info("readRules"+" offset = "+str(offset)+" length = "+str(length))
    hbCommand = HausBusCommand(self.objectId, 10, "readRules")
    hbCommand.addWord(offset)
    hbCommand.addWord(length)
    hbCommand.send()
    logging.info("returns")

  """
  @param offset offset im Gesamtregelblock.
  @param data .
  """
  def RulesData(self, offset:int, data:bytearray):
    logging.info("RulesData"+" offset = "+str(offset)+" data = "+str(data))
    hbCommand = HausBusCommand(self.objectId, 134, "RulesData")
    hbCommand.addWord(offset)
    hbCommand.addBlob(data)
    hbCommand.send()
    logging.info("returns")

  """
  @param weektime .
  """
  def evTime(self, weektime:WeekTime=None
):
    logging.info("evTime"+" weektime = "+str(weektime))
    hbCommand = HausBusCommand(self.objectId, 200, "evTime")
    hbCommand.addWord(weektime.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param deviceId neue ID.
  """
  def evNewDeviceId(self, deviceId:int):
    logging.info("evNewDeviceId"+" deviceId = "+str(deviceId))
    hbCommand = HausBusCommand(self.objectId, 201, "evNewDeviceId")
    hbCommand.addWord(deviceId)
    hbCommand.send()
    logging.info("returns")

  """
  @param reason Grund fuer dieses Event.
  """
  def evStarted(self, reason:EReason):
    logging.info("evStarted"+" reason = "+str(reason))
    hbCommand = HausBusCommand(self.objectId, 202, "evStarted")
    hbCommand.addByte(reason.value)
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
  """
  def getTime(self):
    logging.info("getTime")
    hbCommand = HausBusCommand(self.objectId, 126, "getTime")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param weekTime .
  """
  def setTime(self, weekTime:WeekTime=None
):
    logging.info("setTime"+" weekTime = "+str(weekTime))
    hbCommand = HausBusCommand(self.objectId, 125, "setTime")
    hbCommand.addWord(weekTime.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param weekTime .
  """
  def Time(self, weekTime:WeekTime=None
):
    logging.info("Time"+" weekTime = "+str(weekTime))
    hbCommand = HausBusCommand(self.objectId, 198, "Time")
    hbCommand.addWord(weekTime.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param index Index des abzufragenden Regelzustandes auf dem Controller.
  """
  def getRuleState(self, index:int):
    logging.info("getRuleState"+" index = "+str(index))
    hbCommand = HausBusCommand(self.objectId, 12, "getRuleState")
    hbCommand.addByte(index)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param index Index des zu setzenden Regelzustandes auf dem Controller..
  @param state Der Zustand wird gesetzt ohne die Aktionen auszufuehren..
  """
  def setRuleState(self, index:int, state:int):
    logging.info("setRuleState"+" index = "+str(index)+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 11, "setRuleState")
    hbCommand.addByte(index)
    hbCommand.addByte(state)
    hbCommand.send()
    logging.info("returns")

  """
  @param indexRule Index der Regel im Controller..
  @param indexElement Index des auszufuehrenden Regelelementes. Alle Aktionen werden ausgefuehrt und der neue Zustand eingenommen..
  """
  def triggerRuleElement(self, indexRule:int, indexElement:int):
    logging.info("triggerRuleElement"+" indexRule = "+str(indexRule)+" indexElement = "+str(indexElement))
    hbCommand = HausBusCommand(self.objectId, 13, "triggerRuleElement")
    hbCommand.addByte(indexRule)
    hbCommand.addByte(indexElement)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Index der abgefragten Regel.
  @param state Regelzustand.
  """
  def RuleState(self, index:int, state:int):
    logging.info("RuleState"+" index = "+str(index)+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 135, "RuleState")
    hbCommand.addByte(index)
    hbCommand.addByte(state)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Gruppenindex.
  @param member Gruppenteilnehmer 0-15.
  @param state Zustand des Teilnehmers 0=AUS.
  @param triggerBits Anzahl der Teilnehmer die gesetzt sein muessen damit evGroupOn erzeugt wird.
  """
  def setUnitGroupState(self, index:int, member:int, state:int, triggerBits:int):
    logging.info("setUnitGroupState"+" index = "+str(index)+" member = "+str(member)+" state = "+str(state)+" triggerBits = "+str(triggerBits))
    hbCommand = HausBusCommand(self.objectId, 14, "setUnitGroupState")
    hbCommand.addByte(index)
    hbCommand.addByte(member)
    hbCommand.addByte(state)
    hbCommand.addByte(triggerBits)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Gruppenindex.
  @param status Status der Bits in der logischen Gruppe..
  """
  def evGroupOn(self, index:int, status:int):
    logging.info("evGroupOn"+" index = "+str(index)+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 203, "evGroupOn")
    hbCommand.addByte(index)
    hbCommand.addWord(status)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Gruppenindex.
  @param status Status der Bits in der logischen Gruppe..
  """
  def evGroupOff(self, index:int, status:int):
    logging.info("evGroupOff"+" index = "+str(index)+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 205, "evGroupOff")
    hbCommand.addByte(index)
    hbCommand.addWord(status)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Gruppenindex.
  @param status Status der Bits in der logischen Gruppe..
  """
  def evGroupUndefined(self, index:int, status:int):
    logging.info("evGroupUndefined"+" index = "+str(index)+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 204, "evGroupUndefined")
    hbCommand.addByte(index)
    hbCommand.addWord(status)
    hbCommand.send()
    logging.info("returns")

  """
  @param ruleIndex .
  @param elementIndex .
  """
  def TriggeredRule(self, ruleIndex:int, elementIndex:int):
    logging.info("TriggeredRule"+" ruleIndex = "+str(ruleIndex)+" elementIndex = "+str(elementIndex))
    hbCommand = HausBusCommand(self.objectId, 136, "TriggeredRule")
    hbCommand.addByte(ruleIndex)
    hbCommand.addByte(elementIndex)
    hbCommand.send()
    logging.info("returns")

  """
  @param option SEND_TRIGGERED_RULE_EVENT: generiert ein Event zu einer aktivierten Regel\r\nREAD_ONLY_GATEWAYS: schaltet das Versenden saemtlicher Nachrichten ab. Eingehende Nachrichten werden verarbeitet\r\nREPORT_INTERNAL_TEMPERATURE: aktiviert den internen TemperaturSensor des Prozessors ungenau\r\nSEND_ZERO_CROSS_DATA: sendet im Sekundentakt aufgezeichnete Daten zur Nulldurchganserkennung bei Dimmer-Modulen.
  """
  def setDebugOptions(self, option:MOption):
    logging.info("setDebugOptions"+" option = "+str(option))
    hbCommand = HausBusCommand(self.objectId, 124, "setDebugOptions")
    hbCommand.addByte(option.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param timeDifference Abweichung der internen Wochenzeit in Minuten Achtung: Vorzeichenbehaftetes Byte. 255 entspricht -1.
  """
  def TimeDifference(self, timeDifference:int):
    logging.info("TimeDifference"+" timeDifference = "+str(timeDifference))
    hbCommand = HausBusCommand(self.objectId, 197, "TimeDifference")
    hbCommand.addByte(timeDifference)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evDay(self):
    logging.info("evDay")
    hbCommand = HausBusCommand(self.objectId, 206, "evDay")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evNight(self):
    logging.info("evNight")
    hbCommand = HausBusCommand(self.objectId, 207, "evNight")
    hbCommand.send()
    logging.info("returns")

  """
  @param sunriseTime Zeit fuer den Sonnenaufgang..
  @param sunsetTime Zeit fuer den Sonnenuntergang..
  """
  def setSunTimes(self, sunriseTime:WeekTime=None
, sunsetTime:WeekTime=None
):
    logging.info("setSunTimes"+" sunriseTime = "+str(sunriseTime)+" sunsetTime = "+str(sunsetTime))
    hbCommand = HausBusCommand(self.objectId, 15, "setSunTimes")
    hbCommand.addWord(sunriseTime.getValue())
    hbCommand.addWord(sunsetTime.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param type Hier wird der Typ der Variable.
  @param index Die Variablen liegen mehrfach vor 32xBIT.
  @param value Die Systemvariable wird mit diesem Wert belegt..
  """
  def setSystemVariable(self, type:EType, index:int, value:int):
    logging.info("setSystemVariable"+" type = "+str(type)+" index = "+str(index)+" value = "+str(value))
    hbCommand = HausBusCommand(self.objectId, 16, "setSystemVariable")
    hbCommand.addByte(type.value)
    hbCommand.addByte(index)
    hbCommand.addWord(value)
    hbCommand.send()
    logging.info("returns")

  """
  @param type Hier wird der Typ der Variable.
  @param index Die Variablen liegen mehrfach vor 32xBIT.
  """
  def getSystemVariable(self, type:EType, index:int):
    logging.info("getSystemVariable"+" type = "+str(type)+" index = "+str(index))
    hbCommand = HausBusCommand(self.objectId, 17, "getSystemVariable")
    hbCommand.addByte(type.value)
    hbCommand.addByte(index)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param type Gibt den Typ der Variable an.
  @param index Die Variablen liegen mehrfach vor 32xBIT.
  @param value Der Wert der Systemvariable..
  """
  def SystemVariable(self, type:EType, index:int, value:int):
    logging.info("SystemVariable"+" type = "+str(type)+" index = "+str(index)+" value = "+str(value))
    hbCommand = HausBusCommand(self.objectId, 137, "SystemVariable")
    hbCommand.addByte(type.value)
    hbCommand.addByte(index)
    hbCommand.addWord(value)
    hbCommand.send()
    logging.info("returns")

  """
  @param index Index der logischen Gruppe in diesem Controller.
  """
  def getUnitGroupStatus(self, index:int):
    logging.info("getUnitGroupStatus"+" index = "+str(index))
    hbCommand = HausBusCommand(self.objectId, 18, "getUnitGroupStatus")
    hbCommand.addByte(index)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param index Index der logischen Gruppe in diesem Controller.
  @param status Status der Bits in der logischen Gruppe..
  """
  def UnitGroupStatus(self, index:int, status:int):
    logging.info("UnitGroupStatus"+" index = "+str(index)+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 138, "UnitGroupStatus")
    hbCommand.addByte(index)
    hbCommand.addWord(status)
    hbCommand.send()
    logging.info("returns")

  """
  @param consoleString Debug Ausgaben bei spezieller Firmware zur Fehlersuche.
  """
  def evConsole(self, consoleString:str):
    logging.info("evConsole"+" consoleString = "+str(consoleString))
    hbCommand = HausBusCommand(self.objectId, 250, "evConsole")
    hbCommand.addString(consoleString)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evResetWifi(self):
    logging.info("evResetWifi")
    hbCommand = HausBusCommand(self.objectId, 208, "evResetWifi")
    hbCommand.send()
    logging.info("returns")

  """
  @param channel PWM-Kanal.
  @param lowTime0 .
  @param lowTime1 .
  @param lowTime2 .
  @param lowTime3 .
  @param lowTime4 .
  @param lowTime5 .
  @param lowTime6 .
  @param lowTime7 .
  @param lowTime8 .
  @param lowTime9 .
  @param lowTime10 .
  @param lowTime11 .
  @param lowTime12 .
  @param lowTime13 .
  @param lowTime14 .
  @param lowTime15 .
  @param pulsWidth0 .
  @param pulsWidth1 .
  @param pulsWidth2 .
  @param pulsWidth3 .
  @param pulsWidth4 .
  @param pulsWidth5 .
  @param pulsWidth6 .
  @param pulsWidth7 .
  @param pulsWidth8 .
  @param pulsWidth9 .
  @param pulsWidth10 .
  @param pulsWidth11 .
  @param pulsWidth12 .
  @param pulsWidth13 .
  @param pulsWidth14 .
  @param pulsWidth15 .
  """
  def evZeroCrossData(self, channel:int, lowTime0:int, lowTime1:int, lowTime2:int, lowTime3:int, lowTime4:int, lowTime5:int, lowTime6:int, lowTime7:int, lowTime8:int, lowTime9:int, lowTime10:int, lowTime11:int, lowTime12:int, lowTime13:int, lowTime14:int, lowTime15:int, pulsWidth0:int, pulsWidth1:int, pulsWidth2:int, pulsWidth3:int, pulsWidth4:int, pulsWidth5:int, pulsWidth6:int, pulsWidth7:int, pulsWidth8:int, pulsWidth9:int, pulsWidth10:int, pulsWidth11:int, pulsWidth12:int, pulsWidth13:int, pulsWidth14:int, pulsWidth15:int):
    logging.info("evZeroCrossData"+" channel = "+str(channel)+" lowTime0 = "+str(lowTime0)+" lowTime1 = "+str(lowTime1)+" lowTime2 = "+str(lowTime2)+" lowTime3 = "+str(lowTime3)+" lowTime4 = "+str(lowTime4)+" lowTime5 = "+str(lowTime5)+" lowTime6 = "+str(lowTime6)+" lowTime7 = "+str(lowTime7)+" lowTime8 = "+str(lowTime8)+" lowTime9 = "+str(lowTime9)+" lowTime10 = "+str(lowTime10)+" lowTime11 = "+str(lowTime11)+" lowTime12 = "+str(lowTime12)+" lowTime13 = "+str(lowTime13)+" lowTime14 = "+str(lowTime14)+" lowTime15 = "+str(lowTime15)+" pulsWidth0 = "+str(pulsWidth0)+" pulsWidth1 = "+str(pulsWidth1)+" pulsWidth2 = "+str(pulsWidth2)+" pulsWidth3 = "+str(pulsWidth3)+" pulsWidth4 = "+str(pulsWidth4)+" pulsWidth5 = "+str(pulsWidth5)+" pulsWidth6 = "+str(pulsWidth6)+" pulsWidth7 = "+str(pulsWidth7)+" pulsWidth8 = "+str(pulsWidth8)+" pulsWidth9 = "+str(pulsWidth9)+" pulsWidth10 = "+str(pulsWidth10)+" pulsWidth11 = "+str(pulsWidth11)+" pulsWidth12 = "+str(pulsWidth12)+" pulsWidth13 = "+str(pulsWidth13)+" pulsWidth14 = "+str(pulsWidth14)+" pulsWidth15 = "+str(pulsWidth15))
    hbCommand = HausBusCommand(self.objectId, 209, "evZeroCrossData")
    hbCommand.addByte(channel)
    hbCommand.addWord(lowTime0)
    hbCommand.addWord(lowTime1)
    hbCommand.addWord(lowTime2)
    hbCommand.addWord(lowTime3)
    hbCommand.addWord(lowTime4)
    hbCommand.addWord(lowTime5)
    hbCommand.addWord(lowTime6)
    hbCommand.addWord(lowTime7)
    hbCommand.addWord(lowTime8)
    hbCommand.addWord(lowTime9)
    hbCommand.addWord(lowTime10)
    hbCommand.addWord(lowTime11)
    hbCommand.addWord(lowTime12)
    hbCommand.addWord(lowTime13)
    hbCommand.addWord(lowTime14)
    hbCommand.addWord(lowTime15)
    hbCommand.addWord(pulsWidth0)
    hbCommand.addWord(pulsWidth1)
    hbCommand.addWord(pulsWidth2)
    hbCommand.addWord(pulsWidth3)
    hbCommand.addWord(pulsWidth4)
    hbCommand.addWord(pulsWidth5)
    hbCommand.addWord(pulsWidth6)
    hbCommand.addWord(pulsWidth7)
    hbCommand.addWord(pulsWidth8)
    hbCommand.addWord(pulsWidth9)
    hbCommand.addWord(pulsWidth10)
    hbCommand.addWord(pulsWidth11)
    hbCommand.addWord(pulsWidth12)
    hbCommand.addWord(pulsWidth13)
    hbCommand.addWord(pulsWidth14)
    hbCommand.addWord(pulsWidth15)
    hbCommand.send()
    logging.info("returns")

  """
  @param featureId Zusatzfunktion.
  @param key Der Schluessel mit dem die Zusatzfunktion aktiviert werden soll..
  """
  def enableFeature(self, featureId:EFeatureId, key:str):
    logging.info("enableFeature"+" featureId = "+str(featureId)+" key = "+str(key))
    hbCommand = HausBusCommand(self.objectId, 19, "enableFeature")
    hbCommand.addByte(featureId.value)
    hbCommand.addString(key)
    hbCommand.send()
    logging.info("returns")

  """
  @param type Hier wird der Typ der Variable.
  @param index Die Variablen liegen mehrfach vor 32xBIT.
  @param value Die Systemvariable hat nun diesen Wert erhalten..
  """
  def evSystemVariableChanged(self, type:EType, index:int, value:int):
    logging.info("evSystemVariableChanged"+" type = "+str(type)+" index = "+str(index)+" value = "+str(value))
    hbCommand = HausBusCommand(self.objectId, 210, "evSystemVariableChanged")
    hbCommand.addByte(type.value)
    hbCommand.addByte(index)
    hbCommand.addWord(value)
    hbCommand.send()
    logging.info("returns")


