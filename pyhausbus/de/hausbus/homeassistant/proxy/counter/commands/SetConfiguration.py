from pyhausbus.de.hausbus.homeassistant.proxy.counter.params.MMode import MMode
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 35
  FUNCTION_ID = 1

  def __init__(self,mode:MMode, debounceTime:int, reportTime:int, scaleFaktor:int):
    self.mode=mode
    self.debounceTime=debounceTime
    self.reportTime=reportTime
    self.scaleFaktor=scaleFaktor


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(MMode._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(mode={self.mode}, debounceTime={self.debounceTime}, reportTime={self.reportTime}, scaleFaktor={self.scaleFaktor})"

  '''
  @param mode increment: 1 = Zaehler inkrementieren.
  '''
  def getMode(self) -> MMode:
    return self.mode

  '''
  @param debounceTime 0 - 255[ms].
  '''
  def getDebounceTime(self):
    return self.debounceTime

  '''
  @param reportTime Zeitintervall in Minuten nach dem der Zaehler den aktuellen Stand meldet.
  '''
  def getReportTime(self):
    return self.reportTime

  '''
  @param scaleFaktor Anzahl Impulse pro Einheit z.B. pro kWh.
  '''
  def getScaleFaktor(self):
    return self.scaleFaktor



