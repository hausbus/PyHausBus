from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EType import EType
import pyhausbus.HausBusUtils as HausBusUtils

class GetSystemVariable:
  CLASS_ID = 0
  FUNCTION_ID = 17

  def __init__(self,type:EType, index:int):
    self.type=type
    self.index=index


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetSystemVariable(EType._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"GetSystemVariable(type={self.type}, index={self.index})"

  '''
  @param type Hier wird der Typ der Variable.
  '''
  def getType(self):
    return self.type

  '''
  @param index Die Variablen liegen mehrfach vor 32xBIT.
  '''
  def getIndex(self):
    return self.index



