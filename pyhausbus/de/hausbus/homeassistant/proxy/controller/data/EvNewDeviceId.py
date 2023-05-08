import pyhausbus.HausBusUtils as HausBusUtils

class EvNewDeviceId:
  CLASS_ID = 0
  FUNCTION_ID = 201

  def __init__(self,deviceId:int):
    self.deviceId=deviceId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvNewDeviceId(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvNewDeviceId(deviceId={self.deviceId})"

  '''
  @param deviceId neue ID.
  '''
  def getDeviceId(self):
    return self.deviceId



