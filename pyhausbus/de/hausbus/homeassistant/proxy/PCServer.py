from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils

class PCServer(ABusFeature):
  CLASS_ID:int = 1

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return PCServer(HausBusUtils.getObjectId(deviceId, 1, instanceId))

  """
  @param command .
  """
  def exec(self, command:str):
    LOGGER.debug("exec"+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 0, "exec")
    hbCommand.addString(command)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param varId .
  @param varValue .
  """
  def setVariable(self, varId:int, varValue:int):
    LOGGER.debug("setVariable"+" varId = "+str(varId)+" varValue = "+str(varValue))
    hbCommand = HausBusCommand(self.objectId, 126, "setVariable")
    hbCommand.addByte(varId)
    hbCommand.addByte(varValue)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def shutdown(self):
    LOGGER.debug("shutdown")
    hbCommand = HausBusCommand(self.objectId, 11, "shutdown")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def restart(self):
    LOGGER.debug("restart")
    hbCommand = HausBusCommand(self.objectId, 12, "restart")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def quit(self):
    LOGGER.debug("quit")
    hbCommand = HausBusCommand(self.objectId, 20, "quit")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOnline(self):
    LOGGER.debug("evOnline")
    hbCommand = HausBusCommand(self.objectId, 200, "evOnline")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evOffline(self):
    LOGGER.debug("evOffline")
    hbCommand = HausBusCommand(self.objectId, 201, "evOffline")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def standby(self):
    LOGGER.debug("standby")
    hbCommand = HausBusCommand(self.objectId, 10, "standby")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def reloadUserPlugin(self):
    LOGGER.debug("reloadUserPlugin")
    hbCommand = HausBusCommand(self.objectId, 13, "reloadUserPlugin")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


