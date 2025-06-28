from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.params.EPin import EPin
from pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.params.EErrorCode import EErrorCode

class DigitalPort(ABusFeature):
  CLASS_ID:int = 15

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return DigitalPort(HausBusUtils.getObjectId(deviceId, 15, instanceId))

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param pin0 .
  @param pin1 .
  @param pin2 .
  @param pin3 .
  @param pin4 .
  @param pin5 .
  @param pin6 .
  @param pin7 .
  """
  def setConfiguration(self, pin0:EPin, pin1:EPin, pin2:EPin, pin3:EPin, pin4:EPin, pin5:EPin, pin6:EPin, pin7:EPin):
    LOGGER.debug("setConfiguration"+" pin0 = "+str(pin0)+" pin1 = "+str(pin1)+" pin2 = "+str(pin2)+" pin3 = "+str(pin3)+" pin4 = "+str(pin4)+" pin5 = "+str(pin5)+" pin6 = "+str(pin6)+" pin7 = "+str(pin7))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(pin0.value)
    hbCommand.addByte(pin1.value)
    hbCommand.addByte(pin2.value)
    hbCommand.addByte(pin3.value)
    hbCommand.addByte(pin4.value)
    hbCommand.addByte(pin5.value)
    hbCommand.addByte(pin6.value)
    hbCommand.addByte(pin7.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param pin0 .
  @param pin1 .
  @param pin2 .
  @param pin3 .
  @param pin4 .
  @param pin5 .
  @param pin6 .
  @param pin7 .
  """
  def Configuration(self, pin0:EPin, pin1:EPin, pin2:EPin, pin3:EPin, pin4:EPin, pin5:EPin, pin6:EPin, pin7:EPin):
    LOGGER.debug("Configuration"+" pin0 = "+str(pin0)+" pin1 = "+str(pin1)+" pin2 = "+str(pin2)+" pin3 = "+str(pin3)+" pin4 = "+str(pin4)+" pin5 = "+str(pin5)+" pin6 = "+str(pin6)+" pin7 = "+str(pin7))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(pin0.value)
    hbCommand.addByte(pin1.value)
    hbCommand.addByte(pin2.value)
    hbCommand.addByte(pin3.value)
    hbCommand.addByte(pin4.value)
    hbCommand.addByte(pin5.value)
    hbCommand.addByte(pin6.value)
    hbCommand.addByte(pin7.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


