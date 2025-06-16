import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 164
  FUNCTION_ID = 1

  def __init__(self,SSID:str, Password:str, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    self.SSID=SSID
    self.Password=Password
    self.Server_Port=Server_Port
    self.Server_IP0=Server_IP0
    self.Server_IP1=Server_IP1
    self.Server_IP2=Server_IP2
    self.Server_IP3=Server_IP3


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToString(dataIn, offset), HausBusUtils.bytesToString(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(SSID={self.SSID}, Password={self.Password}, Server_Port={self.Server_Port}, Server_IP0={self.Server_IP0}, Server_IP1={self.Server_IP1}, Server_IP2={self.Server_IP2}, Server_IP3={self.Server_IP3})"

  '''
  @param SSID .
  '''
  def getSSID(self):
    return self.SSID

  '''
  @param Password .
  '''
  def getPassword(self):
    return self.Password

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



