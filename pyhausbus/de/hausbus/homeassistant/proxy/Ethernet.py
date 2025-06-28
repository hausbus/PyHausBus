from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.ethernet.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.ethernet.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.ethernet.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.ethernet.data.CurrentIp import CurrentIp

class Ethernet(ABusFeature):
  CLASS_ID:int = 162

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Ethernet(HausBusUtils.getObjectId(deviceId, 162, instanceId))

  """
  @param mac5 .
  @param mac4 .
  @param mac3 .
  @param mac2 .
  @param mac1 .
  @param mac0 .
  """
  def wakeUpDevice(self, mac5:int, mac4:int, mac3:int, mac2:int, mac1:int, mac0:int):
    LOGGER.debug("wakeUpDevice"+" mac5 = "+str(mac5)+" mac4 = "+str(mac4)+" mac3 = "+str(mac3)+" mac2 = "+str(mac2)+" mac1 = "+str(mac1)+" mac0 = "+str(mac0))
    hbCommand = HausBusCommand(self.objectId, 2, "wakeUpDevice")
    hbCommand.addByte(mac5)
    hbCommand.addByte(mac4)
    hbCommand.addByte(mac3)
    hbCommand.addByte(mac2)
    hbCommand.addByte(mac1)
    hbCommand.addByte(mac0)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param IP0 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  @param IP1 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  @param IP2 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  @param IP3 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  @param options .
  @param Server_Port Zusaetzlicher Port fuer die Homeserverfunktionen z.B 15557 fuer Loxone oder 5855 f?r IOBroker.
  @param Server_IP0 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP1 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP2 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP3 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  """
  def Configuration(self, IP0:int, IP1:int, IP2:int, IP3:int, options:MOptions, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    LOGGER.debug("Configuration"+" IP0 = "+str(IP0)+" IP1 = "+str(IP1)+" IP2 = "+str(IP2)+" IP3 = "+str(IP3)+" options = "+str(options)+" Server_Port = "+str(Server_Port)+" Server_IP0 = "+str(Server_IP0)+" Server_IP1 = "+str(Server_IP1)+" Server_IP2 = "+str(Server_IP2)+" Server_IP3 = "+str(Server_IP3))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(IP0)
    hbCommand.addByte(IP1)
    hbCommand.addByte(IP2)
    hbCommand.addByte(IP3)
    hbCommand.addByte(options.getValue())
    hbCommand.addWord(Server_Port)
    hbCommand.addByte(Server_IP0)
    hbCommand.addByte(Server_IP1)
    hbCommand.addByte(Server_IP2)
    hbCommand.addByte(Server_IP3)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param IP0 .
  @param IP1 .
  @param IP2 .
  @param IP3 .
  @param options .
  @param Server_Port Zusaetzlicher Port fuer die Homeserverfunktionen z.B 15557 fuer Loxone oder 5855 f?r IOBroker.
  @param Server_IP0 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP1 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP2 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP3 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  """
  def setConfiguration(self, IP0:int, IP1:int, IP2:int, IP3:int, options:MOptions, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    LOGGER.debug("setConfiguration"+" IP0 = "+str(IP0)+" IP1 = "+str(IP1)+" IP2 = "+str(IP2)+" IP3 = "+str(IP3)+" options = "+str(options)+" Server_Port = "+str(Server_Port)+" Server_IP0 = "+str(Server_IP0)+" Server_IP1 = "+str(Server_IP1)+" Server_IP2 = "+str(Server_IP2)+" Server_IP3 = "+str(Server_IP3))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(IP0)
    hbCommand.addByte(IP1)
    hbCommand.addByte(IP2)
    hbCommand.addByte(IP3)
    hbCommand.addByte(options.getValue())
    hbCommand.addWord(Server_Port)
    hbCommand.addByte(Server_IP0)
    hbCommand.addByte(Server_IP1)
    hbCommand.addByte(Server_IP2)
    hbCommand.addByte(Server_IP3)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
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

  """
  @param IP0 .
  @param IP1 .
  @param IP2 .
  @param IP3 .
  """
  def CurrentIp(self, IP0:int, IP1:int, IP2:int, IP3:int):
    LOGGER.debug("CurrentIp"+" IP0 = "+str(IP0)+" IP1 = "+str(IP1)+" IP2 = "+str(IP2)+" IP3 = "+str(IP3))
    hbCommand = HausBusCommand(self.objectId, 129, "CurrentIp")
    hbCommand.addByte(IP0)
    hbCommand.addByte(IP1)
    hbCommand.addByte(IP2)
    hbCommand.addByte(IP3)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getCurrentIp(self):
    LOGGER.debug("getCurrentIp")
    hbCommand = HausBusCommand(self.objectId, 3, "getCurrentIp")
    ResultWorker()._setResultInfo(CurrentIp,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


