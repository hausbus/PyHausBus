from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EReason import EReason
import pyhausbus.HausBusUtils as HausBusUtils

class EvStarted:
  CLASS_ID = 0
  FUNCTION_ID = 202

  def __init__(self,reason:EReason):
    self.reason=reason


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStarted(EReason._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvStarted(reason={self.reason})"

  '''
  @param reason Grund fuer dieses Event.
  '''
  def getReason(self):
    return self.reason



