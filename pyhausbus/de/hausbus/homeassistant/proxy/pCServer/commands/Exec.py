import pyhausbus.HausBusUtils as HausBusUtils

class Exec:
  CLASS_ID = 1
  FUNCTION_ID = 0

  def __init__(self,command:str):
    self.command=command


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Exec(HausBusUtils.bytesToString(dataIn, offset))

  def __str__(self):
    return f"Exec(command={self.command})"

  '''
  @param command .
  '''
  def getCommand(self):
    return self.command



