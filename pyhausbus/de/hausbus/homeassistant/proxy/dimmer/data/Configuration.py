from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EMode import EMode
import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 17
  FUNCTION_ID = 128

  def __init__(self,mode:EMode, fadingTime:int, dimmingTime:int, dimmingRangeStart:int, dimmingRangeEnd:int):
    self.mode=mode
    self.fadingTime=fadingTime
    self.dimmingTime=dimmingTime
    self.dimmingRangeStart=dimmingRangeStart
    self.dimmingRangeEnd=dimmingRangeEnd


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(EMode._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Configuration(mode={self.mode}, fadingTime={self.fadingTime}, dimmingTime={self.dimmingTime}, dimmingRangeStart={self.dimmingRangeStart}, dimmingRangeEnd={self.dimmingRangeEnd})"

  '''
  @param mode DIMM_CR: Dimmer arbeitet mit Phasenabschnitt\r\nDIMM_L: Dimmer arbeitet mit Phasenanschnitt\r\nSWITCH: Dimmer schaltet nur keine Dimmfunktion\r\n\r\nACHTUNG: EIN FALSCHER MODE.
  '''
  def getMode(self):
    return self.mode

  '''
  @param fadingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu schalten.
  '''
  def getFadingTime(self):
    return self.fadingTime

  '''
  @param dimmingTime Zeit a 50ms um zwischen den unterschiedlichen Helligkeitsstufen zu dimmen.
  '''
  def getDimmingTime(self):
    return self.dimmingTime

  '''
  @param dimmingRangeStart Startwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  '''
  def getDimmingRangeStart(self):
    return self.dimmingRangeStart

  '''
  @param dimmingRangeEnd Endwert des Helligkeitbereiches in dem gedimmt werden soll. 0-100%.
  '''
  def getDimmingRangeEnd(self):
    return self.dimmingRangeEnd



