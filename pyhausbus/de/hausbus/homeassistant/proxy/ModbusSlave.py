from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.modbusSlave.data.Configuration import Configuration

class ModbusSlave(ABusFeature):
  CLASS_ID:int = 14

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return ModbusSlave(HausBusUtils.getObjectId(deviceId, 14, instanceId))

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()


  """
  @param rtuGatewayDeviceId ID des Geraetes mit dem RTU Gateway.
  """
  def setConfiguration(self, rtuGatewayDeviceId:int):
    LOGGER.debug("setConfiguration"+" rtuGatewayDeviceId = "+str(rtuGatewayDeviceId))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addWord(rtuGatewayDeviceId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()


  """
  @param rtuGatewayDeviceId ID des Geraetes mit dem RTU Gateway.
  """
  def Configuration(self, rtuGatewayDeviceId:int):
    LOGGER.debug("Configuration"+" rtuGatewayDeviceId = "+str(rtuGatewayDeviceId))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addWord(rtuGatewayDeviceId)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()



