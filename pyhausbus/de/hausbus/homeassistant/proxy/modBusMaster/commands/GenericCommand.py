from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EFunction import EFunction
import pyhausbus.HausBusUtils as HausBusUtils

class GenericCommand:
  CLASS_ID = 45
  FUNCTION_ID = 4

  def __init__(self,node:int, function:EFunction, address:int, data:bytearray):
    self.node=node
    self.function=function
    self.address=address
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GenericCommand(HausBusUtils.bytesToInt(dataIn, offset), EFunction._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"GenericCommand(node={self.node}, function={self.function}, address={self.address}, data={self.data})"

  '''
  @param node Bus-Knoten Geraete-Adresse.
  '''
  def getNode(self):
    return self.node

  '''
  @param function Mod-Bus Funktion.
  '''
  def getFunction(self):
    return self.function

  '''
  @param address Adresse in Geraet.
  '''
  def getAddress(self):
    return self.address

  '''
  @param data Daten.
  '''
  def getData(self):
    return self.data



