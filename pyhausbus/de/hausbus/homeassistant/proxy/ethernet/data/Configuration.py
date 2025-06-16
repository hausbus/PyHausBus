from pyhausbus.de.hausbus.homeassistant.proxy.ethernet.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 162
  FUNCTION_ID = 128

  def __init__(self,IP0:int, IP1:int, IP2:int, IP3:int, options:MOptions, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    self.IP0=IP0
    self.IP1=IP1
    self.IP2=IP2
    self.IP3=IP3
    self.options=options
    self.Server_Port=Server_Port
    self.Server_IP0=Server_IP0
    self.Server_IP1=Server_IP1
    self.Server_IP2=Server_IP2
    self.Server_IP3=Server_IP3


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), MOptions._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Configuration(IP0={self.IP0}, IP1={self.IP1}, IP2={self.IP2}, IP3={self.IP3}, options={self.options}, Server_Port={self.Server_Port}, Server_IP0={self.Server_IP0}, Server_IP1={self.Server_IP1}, Server_IP2={self.Server_IP2}, Server_IP3={self.Server_IP3})"

  '''
  @param IP0 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  '''
  def getIP0(self):
    return self.IP0

  '''
  @param IP1 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  '''
  def getIP1(self):
    return self.IP1

  '''
  @param IP2 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  '''
  def getIP2(self):
    return self.IP2

  '''
  @param IP3 Eigene IP-Adresse im Format IP0.IP1.IP2.IP3.
  '''
  def getIP3(self):
    return self.IP3

  '''
  @param options .
  '''
  def getOptions(self) -> MOptions:
    return self.options

  '''
  @param Server_Port Zusaetzlicher Port fuer die Homeserverfunktionen z.B 15557 fuer Loxone oder 5855 f?r IOBroker.
  '''
  def getServer_Port(self):
    return self.Server_Port

  '''
  @param Server_IP0 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  '''
  def getServer_IP0(self):
    return self.Server_IP0

  '''
  @param Server_IP1 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  '''
  def getServer_IP1(self):
    return self.Server_IP1

  '''
  @param Server_IP2 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  '''
  def getServer_IP2(self):
    return self.Server_IP2

  '''
  @param Server_IP3 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  '''
  def getServer_IP3(self):
    return self.Server_IP3



