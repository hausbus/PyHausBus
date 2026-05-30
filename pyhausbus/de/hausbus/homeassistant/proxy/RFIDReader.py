from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.params.EState import EState
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.LastData import LastData
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.State import State
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.TagMapping import TagMapping

class RFIDReader(ABusFeature):
  CLASS_ID:int = 43

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return RFIDReader(HausBusUtils.getObjectId(deviceId, 43, instanceId))

  """
  """
  def evConnected(self):
    LOGGER.debug("evConnected")
    hbCommand = HausBusCommand(self.objectId, 200, "evConnected")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
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
  @param readerId logische TagID dieser Instanz.
  """
  def setConfiguration(self, readerId:int):
    LOGGER.debug("setConfiguration"+" readerId = "+str(readerId))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addWord(readerId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param state State of the RFID-Reader hardware.
  """
  def State(self, state:EState):
    LOGGER.debug("State"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 129, "State")
    hbCommand.addByte(state.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param tagID ID des erkannten RFID tag.
  """
  def evData(self, tagID:int):
    LOGGER.debug("evData"+" tagID = "+str(tagID))
    hbCommand = HausBusCommand(self.objectId, 201, "evData")
    hbCommand.addDWord(tagID)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  """
  def getLastData(self):
    LOGGER.debug("getLastData")
    hbCommand = HausBusCommand(self.objectId, 3, "getLastData")
    ResultWorker()._setResultInfo(LastData,self.getObjectId())
    hbCommand.send()


  """
  @param tagID last tagID read successfully.
  @param logicalTagId falls tagID in der Mapping-Tabelle steht.
  """
  def LastData(self, tagID:int, logicalTagId:int):
    LOGGER.debug("LastData"+" tagID = "+str(tagID)+" logicalTagId = "+str(logicalTagId))
    hbCommand = HausBusCommand(self.objectId, 130, "LastData")
    hbCommand.addDWord(tagID)
    hbCommand.addWord(logicalTagId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param readerId logische TagId dieser Instanz.
  """
  def Configuration(self, readerId:int):
    LOGGER.debug("Configuration"+" readerId = "+str(readerId))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addWord(readerId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  """
  def getState(self):
    LOGGER.debug("getState")
    hbCommand = HausBusCommand(self.objectId, 2, "getState")
    ResultWorker()._setResultInfo(State,self.getObjectId())
    hbCommand.send()


  """
  @param idx index in der Mapping-Tabelle.
  @param physicalTagId Wenn diese TagId gelesen wird.
  @param logicalTagId logische TagId.
  """
  def setTagMapping(self, idx:int, physicalTagId:int, logicalTagId:int):
    LOGGER.debug("setTagMapping"+" idx = "+str(idx)+" physicalTagId = "+str(physicalTagId)+" logicalTagId = "+str(logicalTagId))
    hbCommand = HausBusCommand(self.objectId, 4, "setTagMapping")
    hbCommand.addByte(idx)
    hbCommand.addDWord(physicalTagId)
    hbCommand.addWord(logicalTagId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param idx index in der Mapping-Tabelle.
  """
  def getTagMapping(self, idx:int):
    LOGGER.debug("getTagMapping"+" idx = "+str(idx))
    hbCommand = HausBusCommand(self.objectId, 5, "getTagMapping")
    hbCommand.addByte(idx)
    ResultWorker()._setResultInfo(TagMapping,self.getObjectId())
    hbCommand.send()


  """
  @param idx Index in der Mapping-Tabelle.
  @param physicalTagId Wenn diese TagId gelesen wird.
  @param logicalTagId logische TagId.
  """
  def TagMapping(self, idx:int, physicalTagId:int, logicalTagId:int):
    LOGGER.debug("TagMapping"+" idx = "+str(idx)+" physicalTagId = "+str(physicalTagId)+" logicalTagId = "+str(logicalTagId))
    hbCommand = HausBusCommand(self.objectId, 131, "TagMapping")
    hbCommand.addByte(idx)
    hbCommand.addDWord(physicalTagId)
    hbCommand.addWord(logicalTagId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param logicalTagId logische ID wenn die physikalische tagID ein Mapping hat.
  """
  def evMappedData(self, logicalTagId:int):
    LOGGER.debug("evMappedData"+" logicalTagId = "+str(logicalTagId))
    hbCommand = HausBusCommand(self.objectId, 202, "evMappedData")
    hbCommand.addWord(logicalTagId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()



