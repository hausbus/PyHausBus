from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EStatus import EStatus
import pyhausbus.HausBusUtils as HausBusUtils

class MemoryStatus:
  CLASS_ID = 0
  FUNCTION_ID = 133

  def __init__(self,status:EStatus, address:int):
    self.status=status
    self.address=address


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return MemoryStatus(EStatus._fromBytes(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"MemoryStatus(status={self.status}, address={self.address})"

  '''
  @param status Status des letzten Speicherzugriffs.
  '''
  def getStatus(self):
    return self.status

  '''
  @param address Speicheradresse zu dem dieser Status gesendet wird..
  '''
  def getAddress(self):
    return self.address



