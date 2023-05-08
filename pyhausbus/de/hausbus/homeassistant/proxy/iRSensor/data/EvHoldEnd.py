import pyhausbus.HausBusUtils as HausBusUtils

class EvHoldEnd:
  CLASS_ID = 33
  FUNCTION_ID = 204

  def __init__(self,address:int, command:int):
    self.address=address
    self.command=command


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvHoldEnd(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvHoldEnd(address={self.address}, command={self.command})"

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



