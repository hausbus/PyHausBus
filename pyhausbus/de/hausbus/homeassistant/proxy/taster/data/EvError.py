import pyhausbus.HausBusUtils as HausBusUtils

class EvError:
  CLASS_ID = 16
  FUNCTION_ID = 255

  def __init__(self,errorCode:int):
    self.errorCode=errorCode


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvError(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvError(errorCode={self.errorCode})"

  '''
  @param errorCode .
  '''
  def getErrorCode(self):
    return self.errorCode



