from pyhausbus.de.hausbus.homeassistant.proxy.currentReader.params.MConfig import MConfig
import pyhausbus.HausBusUtils as HausBusUtils

class EvDebug:
  CLASS_ID = 90
  FUNCTION_ID = 210

  def __init__(self,data:int, type:MConfig):
    self.data=data
    self.type=type


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvDebug(HausBusUtils.bytesToDWord(dataIn, offset), MConfig._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvDebug(data={self.data}, type={self.type})"

  '''
  @param data .
  '''
  def getData(self):
    return self.data

  '''
  @param type .
  '''
  def getType(self) -> MConfig:
    return self.type



