import pyhausbus.HausBusUtils as HausBusUtils

class TriggerRuleElement:
  CLASS_ID = 0
  FUNCTION_ID = 13

  def __init__(self,indexRule:int, indexElement:int):
    self.indexRule=indexRule
    self.indexElement=indexElement


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return TriggerRuleElement(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"TriggerRuleElement(indexRule={self.indexRule}, indexElement={self.indexElement})"

  '''
  @param indexRule Index der Regel im Controller..
  '''
  def getIndexRule(self):
    return self.indexRule

  '''
  @param indexElement Index des auszufuehrenden Regelelementes. Alle Aktionen werden ausgefuehrt und der neue Zustand eingenommen..
  '''
  def getIndexElement(self):
    return self.indexElement



