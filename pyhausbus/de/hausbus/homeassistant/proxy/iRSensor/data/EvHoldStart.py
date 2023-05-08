import pyhausbus.HausBusUtils as HausBusUtils

class EvHoldStart:
  CLASS_ID = 33
  FUNCTION_ID = 203

  def __init__(self,address:int, command:int):
    self.address=address
    self.command=command


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvHoldStart(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvHoldStart(address={self.address}, command={self.command})"

  '''
  @param address IR Adresse.
  '''
  def getAddress(self):
    return self.address

  '''
  @param command IR Kommando.
  '''
  def getCommand(self):
    return self.command



