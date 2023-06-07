import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.params.EState import EState

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
    logging.info("evConnected")
    hbCommand = HausBusCommand(self.objectId, 200, "evConnected")
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
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  """
  def setConfiguration(self):
    logging.info("setConfiguration")
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.send()
    logging.info("returns")

  """
  @param state State of the RFID-Reader hardware.
  """
  def State(self, state:EState):
    logging.info("State"+" state = "+str(state))
    hbCommand = HausBusCommand(self.objectId, 129, "State")
    hbCommand.addByte(state.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param tagID ID of the detected RFID tag.
  """
  def evData(self, tagID:int):
    logging.info("evData"+" tagID = "+str(tagID))
    hbCommand = HausBusCommand(self.objectId, 201, "evData")
    hbCommand.addDWord(tagID)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getLastData(self):
    logging.info("getLastData")
    hbCommand = HausBusCommand(self.objectId, 3, "getLastData")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param tagID last tagID read successfully.
  """
  def LastData(self, tagID:int):
    logging.info("LastData"+" tagID = "+str(tagID))
    hbCommand = HausBusCommand(self.objectId, 130, "LastData")
    hbCommand.addDWord(tagID)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def Configuration(self):
    logging.info("Configuration")
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getState(self):
    logging.info("getState")
    hbCommand = HausBusCommand(self.objectId, 2, "getState")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject


