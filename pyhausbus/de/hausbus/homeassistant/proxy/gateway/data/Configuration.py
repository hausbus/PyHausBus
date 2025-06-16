from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 176
  FUNCTION_ID = 128

  def __init__(self,options:MOptions):
    self.options=options


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(MOptions._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Configuration(options={self.options})"

  '''
  @param options enabled: Dies Gateway ist aktiv und leitet Nachrichten weiter\r\npreferLoxone: Gateway kommuniziert bevorzugt im Loxone-Protokoll\r\nenableConsole: aktiviert das senden von Debugausgaben\r\nmaster: dieses Gateway soll das Bus-Timing verwalten.
  '''
  def getOptions(self) -> MOptions:
    return self.options



