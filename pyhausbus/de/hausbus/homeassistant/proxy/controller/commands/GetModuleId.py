from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MGroupMask import MGroupMask
import pyhausbus.HausBusUtils as HausBusUtils

class GetModuleId:
  CLASS_ID = 0
  FUNCTION_ID = 2

  def __init__(self,index:EIndex, groupMask:MGroupMask):
    self.index=index
    self.groupMask=groupMask


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetModuleId(EIndex._fromBytes(dataIn, offset), MGroupMask._fromBytes(dataIn, offset))

  def __str__(self):
    return f"GetModuleId(index={self.index}, groupMask={self.groupMask})"

  '''
  @param index .
  '''
  def getIndex(self):
    return self.index

  '''
  @param groupMask Selektiert 1-8 Ger?tegruppen.
  '''
  def getGroupMask(self) -> MGroupMask:
    return self.groupMask



