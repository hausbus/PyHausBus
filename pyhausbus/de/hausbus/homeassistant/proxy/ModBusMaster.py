from pyhausbus.HausBusUtils import LOGGER
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.ESensorType import ESensorType

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
  def getConfiguration(self, idx:int):
    LOGGER.debug("getConfiguration"+" idx = "+str(idx))
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.addByte(idx)
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param idx index of the configuration slot.
  @param node Geraeteadresse im ModBus.
  @param sensorType Supported Power-Meter SDM630 / SDM72D / SDM72V2 / ORWE517.
  """
  def setConfiguration(self, idx:int, node:int, sensorType:ESensorType):
    LOGGER.debug("setConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" sensorType = "+str(sensorType))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(sensorType.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param idx index of the configuration slot.
  @param node device node on ModBus.
  @param sensorType Supported Power-Meter SDM630 / SDM72D / SDM72V2 / ORWE517.
  """
  def Configuration(self, idx:int, node:int, sensorType:ESensorType):
    LOGGER.debug("Configuration"+" idx = "+str(idx)+" node = "+str(node)+" sensorType = "+str(sensorType))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(sensorType.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


