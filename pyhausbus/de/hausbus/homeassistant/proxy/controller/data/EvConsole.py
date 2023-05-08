import pyhausbus.HausBusUtils as HausBusUtils

class EvConsole:
  CLASS_ID = 0
  FUNCTION_ID = 250

  def __init__(self,consoleString:str):
    self.consoleString=consoleString


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvConsole(HausBusUtils.bytesToString(dataIn, offset))

  def __str__(self):
    return f"EvConsole(consoleString={self.consoleString})"

  '''
  @param consoleString Debug Ausgaben bei spezieller Firmware zur Fehlersuche.
  '''
  def getConsoleString(self):
    return self.consoleString



