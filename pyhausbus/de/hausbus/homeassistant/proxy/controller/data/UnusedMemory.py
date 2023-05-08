import pyhausbus.HausBusUtils as HausBusUtils

class UnusedMemory:
  CLASS_ID = 0
  FUNCTION_ID = 130

  def __init__(self,freeStack:int, freeHeap:int):
    self.freeStack=freeStack
    self.freeHeap=freeHeap


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return UnusedMemory(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"UnusedMemory(freeStack={self.freeStack}, freeHeap={self.freeHeap})"

  '''
  @param freeStack Anzahl des nicht genutzten Stacks in Bytes..
  '''
  def getFreeStack(self):
    return self.freeStack

  '''
  @param freeHeap Aktuell freier Heap in Bytes..
  '''
  def getFreeHeap(self):
    return self.freeHeap



