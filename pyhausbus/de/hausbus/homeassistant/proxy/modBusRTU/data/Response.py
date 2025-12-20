from pyhausbus.de.hausbus.homeassistant.proxy.modBusRTU.params.EFunction import EFunction
import pyhausbus.HausBusUtils as HausBusUtils

class Response:
  CLASS_ID = 45
  FUNCTION_ID = 130

  def __init__(self,node:int, function:EFunction, data:bytearray):
    self.node=node
    self.function=function
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Response(HausBusUtils.bytesToInt(dataIn, offset), EFunction._fromBytes(dataIn, offset), HausBusUtils.bytesToBlob(dataIn, offset))

  def __str__(self):
    return f"Response(node={self.node}, function={self.function}, data={self.data})"

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
  @param data Daten.
  '''
  def getData(self):
    return self.data



