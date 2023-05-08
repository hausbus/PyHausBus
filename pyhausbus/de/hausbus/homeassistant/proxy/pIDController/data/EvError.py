from pyhausbus.de.hausbus.homeassistant.proxy.pIDController.params.EErrorCode import EErrorCode
import pyhausbus.HausBusUtils as HausBusUtils

class EvError:
  CLASS_ID = 44
  FUNCTION_ID = 255

  def __init__(self,errorCode:EErrorCode):
    self.errorCode=errorCode


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvError(EErrorCode._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvError(errorCode={self.errorCode})"

  '''
  @param errorCode .
  '''
  def getErrorCode(self):
    return self.errorCode



