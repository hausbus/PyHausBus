from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils

class IRSensor(ABusFeature):
  CLASS_ID:int = 33

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return IRSensor(HausBusUtils.getObjectId(deviceId, 33, instanceId))

  """
  """
  def off(self):
    LOGGER.debug("off")
    hbCommand = HausBusCommand(self.objectId, 0, "off")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def on(self):
    LOGGER.debug("on")
    hbCommand = HausBusCommand(self.objectId, 1, "on")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evClicked(self, address:int, command:int):
    LOGGER.debug("evClicked"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 202, "evClicked")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
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
  def evOn(self):
    LOGGER.debug("evOn")
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evHoldStart(self, address:int, command:int):
    LOGGER.debug("evHoldStart"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 203, "evHoldStart")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evHoldEnd(self, address:int, command:int):
    LOGGER.debug("evHoldEnd"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 204, "evHoldEnd")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


