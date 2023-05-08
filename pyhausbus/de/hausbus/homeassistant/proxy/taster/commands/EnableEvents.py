from pyhausbus.de.hausbus.homeassistant.proxy.taster.params.EEnable import EEnable
import pyhausbus.HausBusUtils as HausBusUtils

class EnableEvents:
  CLASS_ID = 16
  FUNCTION_ID = 2

  def __init__(self,enable:EEnable, disabledDuration:int):
    self.enable=enable
    self.disabledDuration=disabledDuration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EnableEvents(EEnable._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EnableEvents(enable={self.enable}, disabledDuration={self.disabledDuration})"

  '''
  @param enable FALSE: Deaktiviert das Versenden von Events\r\nTRUE: Aktiviert das Versenden von Events\r\nINVERT: Invertiert das aktuelle Verhalten.
  '''
  def getEnable(self):
    return self.enable

  '''
  @param disabledDuration Zeit1s-255s f?  ? ? ?r die die Events deaktiviert werden sollen 0 = unendlich \r\nDieser Parameter wirkt nur.
  '''
  def getDisabledDuration(self):
    return self.disabledDuration



