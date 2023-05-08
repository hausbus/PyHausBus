from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MOption import MOption
import pyhausbus.HausBusUtils as HausBusUtils

class SetDebugOptions:
  CLASS_ID = 0
  FUNCTION_ID = 124

  def __init__(self,option:MOption):
    self.option=option


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetDebugOptions(MOption._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetDebugOptions(option={self.option})"

  '''
  @param option SEND_TRIGGERED_RULE_EVENT: generiert ein Event zu einer aktivierten Regel\r\nREAD_ONLY_GATEWAYS: schaltet das Versenden saemtlicher Nachrichten ab. Eingehende Nachrichten werden verarbeitet\r\nREPORT_INTERNAL_TEMPERATURE: aktiviert den internen TemperaturSensor des Prozessors ungenau\r\nSEND_ZERO_CROSS_DATA: sendet im Sekundentakt aufgezeichnete Daten zur Nulldurchganserkennung bei Dimmer-Modulen.
  '''
  def getOption(self) -> MOption:
    return self.option



