from pyhausbus.de.hausbus.homeassistant.proxy.gateway.params.EValue import EValue
import pyhausbus.HausBusUtils as HausBusUtils

class SetPreferLoxone:
  CLASS_ID = 176
  FUNCTION_ID = 2

  def __init__(self,value:EValue):
    self.value=value


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetPreferLoxone(EValue._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetPreferLoxone(value={self.value})"

  '''
  @param value Diese Funktion setzt das Flag \"preferLoxone\" in der Konfiguration entsprechend Persistent..
  '''
  def getValue(self):
    return self.value



