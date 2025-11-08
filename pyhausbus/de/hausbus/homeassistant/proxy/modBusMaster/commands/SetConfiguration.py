from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EBaudrate import EBaudrate
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EDataSetting import EDataSetting
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 45
  FUNCTION_ID = 1

  def __init__(self,baudrate:EBaudrate, dataSetting:EDataSetting, responseTimeout:int):
    self.baudrate=baudrate
    self.dataSetting=dataSetting
    self.responseTimeout=responseTimeout


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(EBaudrate._fromBytes(dataIn, offset), EDataSetting._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(baudrate={self.baudrate}, dataSetting={self.dataSetting}, responseTimeout={self.responseTimeout})"

  '''
  @param baudrate Verbindungsgeschwindigkeit.
  '''
  def getBaudrate(self):
    return self.baudrate

  '''
  @param dataSetting Anzahl Daten-Bits.
  '''
  def getDataSetting(self):
    return self.dataSetting

  '''
  @param responseTimeout Zeit in [ms] um auf eine Antwort zu warten.
  '''
  def getResponseTimeout(self):
    return self.responseTimeout



