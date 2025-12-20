import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 14
  FUNCTION_ID = 1

  def __init__(self,rtuGatewayDeviceId:int):
    self.rtuGatewayDeviceId=rtuGatewayDeviceId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(rtuGatewayDeviceId={self.rtuGatewayDeviceId})"

  '''
  @param rtuGatewayDeviceId ID des Geraetes mit dem RTU Gateway.
  '''
  def getRtuGatewayDeviceId(self):
    return self.rtuGatewayDeviceId



