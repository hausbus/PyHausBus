import pyhausbus.HausBusUtils as HausBusUtils

class TriggeredRule:
  CLASS_ID = 0
  FUNCTION_ID = 136

  def __init__(self,ruleIndex:int, elementIndex:int):
    self.ruleIndex=ruleIndex
    self.elementIndex=elementIndex


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return TriggeredRule(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"TriggeredRule(ruleIndex={self.ruleIndex}, elementIndex={self.elementIndex})"

  '''
  @param ruleIndex .
  '''
  def getRuleIndex(self):
    return self.ruleIndex

  '''
  @param elementIndex .
  '''
  def getElementIndex(self):
    return self.elementIndex



