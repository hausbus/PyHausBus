import pyhausbus.HausBusUtils as HausBusUtils

class AnnounceServer:
  CLASS_ID = 91
  FUNCTION_ID = 1

  def __init__(self,IP0:int, IP1:int, IP2:int, IP3:int, port:int):
    self.IP0=IP0
    self.IP1=IP1
    self.IP2=IP2
    self.IP3=IP3
    self.port=port


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return AnnounceServer(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"AnnounceServer(IP0={self.IP0}, IP1={self.IP1}, IP2={self.IP2}, IP3={self.IP3}, port={self.port})"

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

  '''
  @param port .
  '''
  def getPort(self):
    return self.port



