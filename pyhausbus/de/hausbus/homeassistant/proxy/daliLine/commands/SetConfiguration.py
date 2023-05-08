import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 160
  FUNCTION_ID = 1

  def __init__(self,address0:int, address1:int, address2:int, address3:int):
    self.address0=address0
    self.address1=address1
    self.address2=address2
    self.address3=address3


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(address0={self.address0}, address1={self.address1}, address2={self.address2}, address3={self.address3})"

  '''
  @param address0 .
  '''
  def getAddress0(self):
    return self.address0

  '''
  @param address1 .
  '''
  def getAddress1(self):
    return self.address1

  '''
  @param address2 .
  '''
  def getAddress2(self):
    return self.address2

  '''
  @param address3 .
  '''
  def getAddress3(self):
    return self.address3



