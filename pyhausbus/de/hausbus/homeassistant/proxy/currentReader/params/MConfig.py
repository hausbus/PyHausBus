import pyhausbus.HausBusUtils as HausBusUtils
class MConfig:

  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MConfig(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    return result
  def setEntry(self,name:str, setValue:bool):

  def __str__(self):
    return f"MConfig()"



