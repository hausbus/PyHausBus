import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 14
  FUNCTION_ID = 128

  def __init__(self,rtuGatewayDeviceId:int):
    self.rtuGatewayDeviceId=rtuGatewayDeviceId


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Configuration(rtuGatewayDeviceId={self.rtuGatewayDeviceId})"

  '''
  @param rtuGatewayDeviceId ID des Geraetes mit dem RTU Gateway.
  '''
  def getRtuGatewayDeviceId(self):
    return self.rtuGatewayDeviceId



