import pyhausbus.HausBusUtils as HausBusUtils

class CurrentIp:
  CLASS_ID = 164
  FUNCTION_ID = 129

  def __init__(self,IP0:int, IP1:int, IP2:int, IP3:int):
    self.IP0=IP0
    self.IP1=IP1
    self.IP2=IP2
    self.IP3=IP3


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return CurrentIp(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"CurrentIp({self.IP0}.{self.IP1}.{self.IP2}.{self.IP3})"

  '''
  @param IP0 .
  '''
  def getIP0(self):
    return self.IP0

  '''
  @param IP1 .
  '''
  def getIP1(self):
    return self.IP1

  '''
  @param IP2 .
  '''
  def getIP2(self):
    return self.IP2

  '''
  @param IP3 .
  '''
  def getIP3(self):
    return self.IP3



