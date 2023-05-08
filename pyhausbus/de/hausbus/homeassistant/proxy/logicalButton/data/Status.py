from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.EStatus import EStatus
import pyhausbus.HausBusUtils as HausBusUtils

class Status:
  CLASS_ID = 20
  FUNCTION_ID = 129

  def __init__(self,status:EStatus):
    self.status=status


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Status(EStatus._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Status(status={self.status})"

  '''
  @param status Zustand der Taster LEDs.
  '''
  def getStatus(self):
    return self.status



