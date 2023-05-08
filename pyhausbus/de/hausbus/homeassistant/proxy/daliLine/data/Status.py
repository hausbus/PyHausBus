import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 160
  FUNCTION_ID = 129

  def __init__(self,status:int):
    self.status=status


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Status(status={self.status})"

  '''
  @param status .
  '''
  def getStatus(self):
    return self.status



