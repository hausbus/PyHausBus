from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ERegisterType import ERegisterType
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ESensorType import ESensorType
from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.ESiPrefix import ESiPrefix
import pyhausbus.HausBusUtils as HausBusUtils

class RegisterConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 129

  def __init__(self,idx:int, node:int, registerType:ERegisterType, address:int, sensorType:ESensorType, siPrefix:ESiPrefix):
    self.idx=idx
    self.node=node
    self.registerType=registerType
    self.address=address
    self.sensorType=sensorType
    self.siPrefix=siPrefix


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return RegisterConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), ERegisterType._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), ESensorType._fromBytes(dataIn, offset), ESiPrefix._fromBytes(dataIn, offset))

  def __str__(self):
    return f"RegisterConfiguration(idx={self.idx}, node={self.node}, registerType={self.registerType}, address={self.address}, sensorType={self.sensorType}, siPrefix={self.siPrefix})"

  '''
  @param idx index der Konfiguration.
  '''
  def getIdx(self):
    return self.idx

  '''
  @param node Knoten Nummer im BUS.
  '''
  def getNode(self):
    return self.node

  '''
  @param registerType Unterstuetzte Register Typen.
  '''
  def getRegisterType(self):
    return self.registerType

  '''
  @param address Register Adresse.
  '''
  def getAddress(self):
    return self.address

  '''
  @param sensorType Sensor Typ meldet sich dann mit der entsprechenden Feature-Klasse.
  '''
  def getSensorType(self):
    return self.sensorType

  '''
  @param siPrefix Si-Prefix f?r den Zahlenwert im ModBus-Register.
  '''
  def getSiPrefix(self):
    return self.siPrefix



