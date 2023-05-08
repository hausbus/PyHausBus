from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import EFirmwareId
import pyhausbus.HausBusUtils as HausBusUtils

class ModuleId:
  CLASS_ID = 0
  FUNCTION_ID = 128

  def __init__(self,name:str, size:int, majorRelease:int, minorRelease:int, firmwareId:EFirmwareId):
    self.name=name
    self.size=size
    self.majorRelease=majorRelease
    self.minorRelease=minorRelease
    self.firmwareId=firmwareId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ModuleId(HausBusUtils.bytesToString(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), EFirmwareId._fromBytes(dataIn, offset))

  def __str__(self):
    return f"ModuleId(name={self.name}, size={self.size}, majorRelease={self.majorRelease}, minorRelease={self.minorRelease}, firmwareId={self.firmwareId})"

  '''
  @param name Modulname.
  '''
  def getName(self):
    return self.name

  '''
  @param size Modulgroesse in Bytes.
  '''
  def getSize(self):
    return self.size

  '''
  @param majorRelease Release-Kennung Format major.minor.
  '''
  def getMajorRelease(self):
    return self.majorRelease

  '''
  @param minorRelease Release-Kennung Format major.minor.
  '''
  def getMinorRelease(self):
    return self.minorRelease

  '''
  @param firmwareId Firmware-Kennung.
  '''
  def getFirmwareId(self):
    return self.firmwareId



