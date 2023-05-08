from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EType import EType
import pyhausbus.HausBusUtils as HausBusUtils

class SetSystemVariable:
  CLASS_ID = 0
  FUNCTION_ID = 16

  def __init__(self,type:EType, index:int, value:int):
    self.type=type
    self.index=index
    self.value=value


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetSystemVariable(EType._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetSystemVariable(type={self.type}, index={self.index}, value={self.value})"

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

  '''
  @param value Die Systemvariable wird mit diesem Wert belegt..
  '''
  def getValue(self):
    return self.value



