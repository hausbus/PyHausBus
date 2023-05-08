from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EDirection import EDirection
import pyhausbus.HausBusUtils as HausBusUtils

class Start:
  CLASS_ID = 17
  FUNCTION_ID = 3

  def __init__(self,direction:EDirection):
    self.direction=direction


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Start(EDirection._fromBytes(dataIn, offset))

  def __str__(self):
    return f"Start(direction={self.direction})"

  '''
  @param direction .
  '''
  def getDirection(self):
    return self.direction



