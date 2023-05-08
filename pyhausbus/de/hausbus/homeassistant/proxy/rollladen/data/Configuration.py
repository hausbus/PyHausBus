from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.MOptions import MOptions
import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 18
  FUNCTION_ID = 128

  def __init__(self,closeTime:int, openTime:int, options:MOptions):
    self.closeTime=closeTime
    self.openTime=openTime
    self.options=options


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), MOptions._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Configuration(closeTime={self.closeTime}, openTime={self.openTime}, options={self.options})"

  '''
  @param closeTime Zeit.
  '''
  def getCloseTime(self):
    return self.closeTime

  '''
  @param openTime Zeit.
  '''
  def getOpenTime(self):
    return self.openTime

  '''
  @param options invertDirection: invertiert die Richtung der Ansteuerung des Rollladen.\r\nindependent: behandelt die Relais unabhaengig voneinander d.h. pro Richtung wird nur das jeweilige Relais geschaltet\r\ninvertOutputs: steuert die angeschlossenen Relais mit activLow Logik\r\nenableTracing: Objekt sendet zus?tzliche Events f?r eine Fehlersuche.
  '''
  def getOptions(self) -> MOptions:
    return self.options



