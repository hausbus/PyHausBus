import pyhausbus.HausBusUtils as HausBusUtils

class SetVariable:
  CLASS_ID = 1
  FUNCTION_ID = 126

  def __init__(self,varId:int, varValue:int):
    self.varId=varId
    self.varValue=varValue


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetVariable(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetVariable(varId={self.varId}, varValue={self.varValue})"

  '''
  @param varId .
  '''
  def getVarId(self):
    return self.varId

  '''
  @param varValue .
  '''
  def getVarValue(self):
    return self.varValue



