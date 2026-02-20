from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MGroupMask import MGroupMask
import pyhausbus.HausBusUtils as HausBusUtils

class GetConfiguration:
  CLASS_ID = 0
  FUNCTION_ID = 5

  def __init__(self,groupMask:MGroupMask):
    self.groupMask=groupMask


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GetConfiguration(MGroupMask._fromBytes(dataIn, offset))

  def __str__(self):
    return f"GetConfiguration(groupMask={self.groupMask})"

  '''
  @param groupMask Selektiert 1-8 Ger?tegruppen.
  '''
  def getGroupMask(self) -> MGroupMask:
    return self.groupMask



