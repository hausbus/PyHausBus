from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.params.EEnable import EEnable
import pyhausbus.HausBusUtils as HausBusUtils

class Enable:
  CLASS_ID = 44
  FUNCTION_ID = 3

  def __init__(self,enable:EEnable):
    self.enable=enable


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Enable(EEnable._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Enable(enable={self.enable})"

  '''
  @param enable Reglerverhalten ein/ausschalten.
  '''
  def getEnable(self):
    return self.enable



