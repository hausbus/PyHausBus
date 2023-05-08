import pyhausbus.HausBusUtils as HausBusUtils

class ConnectedDevices:
  CLASS_ID = 176
  FUNCTION_ID = 130

  def __init__(self,deviceIds):
    self.deviceIds=deviceIds


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ConnectedDevices(HausBusUtils.bytesToList(dataIn, offset))

  def __str__(self):
    return f"ConnectedDevices(deviceIds={self.deviceIds})"

  '''
  @param deviceIds .
  '''
  def getDeviceIds(self):
    return self.deviceIds



