import pyhausbus.HausBusUtils as HausBusUtils

class WakeUpDevice:
  CLASS_ID = 164
  FUNCTION_ID = 2

  def __init__(self,mac1:int, mac2:int, mac3:int, mac4:int, mac5:int, mac6:int):
    self.mac1=mac1
    self.mac2=mac2
    self.mac3=mac3
    self.mac4=mac4
    self.mac5=mac5
    self.mac6=mac6


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return WakeUpDevice(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"WakeUpDevice(mac1={self.mac1}, mac2={self.mac2}, mac3={self.mac3}, mac4={self.mac4}, mac5={self.mac5}, mac6={self.mac6})"

  '''
  @param mac1 .
  '''
  def getMac1(self):
    return self.mac1

  '''
  @param mac2 .
  '''
  def getMac2(self):
    return self.mac2

  '''
  @param mac3 .
  '''
  def getMac3(self):
    return self.mac3

  '''
  @param mac4 .
  '''
  def getMac4(self):
    return self.mac4

  '''
  @param mac5 .
  '''
  def getMac5(self):
    return self.mac5

  '''
  @param mac6 .
  '''
  def getMac6(self):
    return self.mac6



