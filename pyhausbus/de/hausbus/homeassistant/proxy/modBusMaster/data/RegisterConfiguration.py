from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EType import EType
import pyhausbus.HausBusUtils as HausBusUtils

class RegisterConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 129

  def __init__(self,idx:int, node:int, type:EType, address:int):
    self.idx=idx
    self.node=node
    self.type=type
    self.address=address


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return RegisterConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), EType._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"RegisterConfiguration(idx={self.idx}, node={self.node}, type={self.type}, address={self.address})"

  '''
  @param idx index of the configuration slot.
  '''
  def getIdx(self):
    return self.idx

  '''
  @param node device node on ModBus.
  '''
  def getNode(self):
    return self.node

  '''
  @param type Unterstuetzte Register Typen.
  '''
  def getType(self):
    return self.type

  '''
  @param address Register Adresse.
  '''
  def getAddress(self):
    return self.address



