from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.ESensorType import ESensorType
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 1

  def __init__(self,idx:int, node:int, sensorType:ESensorType):
    self.idx=idx
    self.node=node
    self.sensorType=sensorType


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), ESensorType._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(idx={self.idx}, node={self.node}, sensorType={self.sensorType})"

  '''
  @param idx index of the configuration slot.
  '''
  def getIdx(self):
    return self.idx

  '''
  @param node Geraeteadresse im ModBus.
  '''
  def getNode(self):
    return self.node

  '''
  @param sensorType Supported Power-Meter SDM630 / SDM72D / SDM72V2 / ORWE517.
  '''
  def getSensorType(self):
    return self.sensorType



