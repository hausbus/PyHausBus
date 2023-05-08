from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EErrorCode import EErrorCode
import pyhausbus.HausBusUtils as HausBusUtils

class EvError:
  CLASS_ID = 17
  FUNCTION_ID = 255

  def __init__(self,errorCode:EErrorCode):
    self.errorCode=errorCode


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvError(EErrorCode._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvError(errorCode={self.errorCode})"

  '''
  @param errorCode NO_ZERO_CROSS_DETECTED: Nulldurchgaenge koennen nicht detektiert werde.
  '''
  def getErrorCode(self):
    return self.errorCode



