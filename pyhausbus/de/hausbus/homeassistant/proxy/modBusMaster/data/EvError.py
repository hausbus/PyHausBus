from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.EErrorCode import EErrorCode
import pyhausbus.HausBusUtils as HausBusUtils

class EvError:
  CLASS_ID = 45
  FUNCTION_ID = 255

  def __init__(self,errorCode:EErrorCode, data:int):
    self.errorCode=errorCode
    self.data=data


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvError(EErrorCode._fromBytes(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvError(errorCode={self.errorCode}, data={self.data})"

  '''
  @param errorCode .
  '''
  def getErrorCode(self):
    return self.errorCode

  '''
  @param data .
  '''
  def getData(self):
    return self.data



