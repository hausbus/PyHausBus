from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
import pyhausbus.HausBusUtils as HausBusUtils

class GetModuleId:
  CLASS_ID = 0
  FUNCTION_ID = 2

  def __init__(self,index:EIndex):
    self.index=index


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetModuleId(EIndex._fromBytes(dataIn, offset))

  def __str__(self):
    return f"GetModuleId(index={self.index})"

  '''
  @param index .
  '''
  def getIndex(self):
    return self.index



