from pyhausbus.de.hausbus.homeassistant.proxy.rollladen.params.EDirection import EDirection
import pyhausbus.HausBusUtils as HausBusUtils

class EvStart:
  CLASS_ID = 18
  FUNCTION_ID = 201

  def __init__(self,direction:EDirection):
    self.direction=direction


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvStart(EDirection._fromBytes(dataIn, offset))

  def __str__(self):
    return f"EvStart(direction={self.direction})"

  '''
  @param direction .
  '''
  def getDirection(self):
    return self.direction



