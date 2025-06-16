import logging
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
    logging.info("exec"+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 0, "exec")
    hbCommand.addString(command)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param varId .
  @param varValue .
  """
  def setVariable(self, varId:int, varValue:int):
    logging.info("setVariable"+" varId = "+str(varId)+" varValue = "+str(varValue))
    hbCommand = HausBusCommand(self.objectId, 126, "setVariable")
    hbCommand.addByte(varId)
    hbCommand.addByte(varValue)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def shutdown(self):
    logging.info("shutdown")
    hbCommand = HausBusCommand(self.objectId, 11, "shutdown")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def restart(self):
    logging.info("restart")
    hbCommand = HausBusCommand(self.objectId, 12, "restart")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def quit(self):
    logging.info("quit")
    hbCommand = HausBusCommand(self.objectId, 20, "quit")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOnline(self):
    logging.info("evOnline")
    hbCommand = HausBusCommand(self.objectId, 200, "evOnline")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOffline(self):
    logging.info("evOffline")
    hbCommand = HausBusCommand(self.objectId, 201, "evOffline")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def standby(self):
    logging.info("standby")
    hbCommand = HausBusCommand(self.objectId, 10, "standby")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def reloadUserPlugin(self):
    logging.info("reloadUserPlugin")
    hbCommand = HausBusCommand(self.objectId, 13, "reloadUserPlugin")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")


