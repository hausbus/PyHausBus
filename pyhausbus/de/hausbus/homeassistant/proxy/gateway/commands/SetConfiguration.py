from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 176
  FUNCTION_ID = 1

  def __init__(self,options:MOptions):
    self.options=options


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(MOptions._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(options={self.options})"

  '''
  @param options enabled: Dies Gateway ist aktiv und leitet Nachrichten weiter\r\npreferLoxone: Gateway kommuniziert bevorzugt im Loxone-Protokoll\r\nenableConsole: aktiviert das senden von Debugausgaben\r\nmaster: dieses Gateway soll das Bus-Timing verwalten\r\n\r\nReservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  '''
  def getOptions(self) -> MOptions:
    return self.options



