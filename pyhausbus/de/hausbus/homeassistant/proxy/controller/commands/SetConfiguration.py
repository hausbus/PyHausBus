from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.MLogicalButtonMask import MLogicalButtonMask
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.ESlotType import ESlotType
import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 0
  FUNCTION_ID = 6

  def __init__(self,startupDelay:int, logicalButtonMask:MLogicalButtonMask, deviceId:int, reportMemoryStatusTime:int, slotType0:ESlotType, slotType1:ESlotType, slotType2:ESlotType, slotType3:ESlotType, slotType4:ESlotType, slotType5:ESlotType, slotType6:ESlotType, slotType7:ESlotType):
    self.startupDelay=startupDelay
    self.logicalButtonMask=logicalButtonMask
    self.deviceId=deviceId
    self.reportMemoryStatusTime=reportMemoryStatusTime
    self.slotType0=slotType0
    self.slotType1=slotType1
    self.slotType2=slotType2
    self.slotType3=slotType3
    self.slotType4=slotType4
    self.slotType5=slotType5
    self.slotType6=slotType6
    self.slotType7=slotType7


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), MLogicalButtonMask._fromBytes(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset), ESlotType._fromBytes(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(startupDelay={self.startupDelay}, logicalButtonMask={self.logicalButtonMask}, deviceId={self.deviceId}, reportMemoryStatusTime={self.reportMemoryStatusTime}, slotType0={self.slotType0}, slotType1={self.slotType1}, slotType2={self.slotType2}, slotType3={self.slotType3}, slotType4={self.slotType4}, slotType5={self.slotType5}, slotType6={self.slotType6}, slotType7={self.slotType7})"

  '''
  @param startupDelay a 10ms.
  '''
  def getStartupDelay(self):
    return self.startupDelay

  '''
  @param logicalButtonMask jedes Bit enspricht einem logischem Taster.
  '''
  def getLogicalButtonMask(self) -> MLogicalButtonMask:
    return self.logicalButtonMask

  '''
  @param deviceId .
  '''
  def getDeviceId(self):
    return self.deviceId

  '''
  @param reportMemoryStatusTime Zeitinterval in Minuten1-255min.
  '''
  def getReportMemoryStatusTime(self):
    return self.reportMemoryStatusTime

  '''
  @param slotType0 .
  '''
  def getSlotType0(self):
    return self.slotType0

  '''
  @param slotType1 .
  '''
  def getSlotType1(self):
    return self.slotType1

  '''
  @param slotType2 .
  '''
  def getSlotType2(self):
    return self.slotType2

  '''
  @param slotType3 .
  '''
  def getSlotType3(self):
    return self.slotType3

  '''
  @param slotType4 .
  '''
  def getSlotType4(self):
    return self.slotType4

  '''
  @param slotType5 .
  '''
  def getSlotType5(self):
    return self.slotType5

  '''
  @param slotType6 .
  '''
  def getSlotType6(self):
    return self.slotType6

  '''
  @param slotType7 .
  '''
  def getSlotType7(self):
    return self.slotType7



