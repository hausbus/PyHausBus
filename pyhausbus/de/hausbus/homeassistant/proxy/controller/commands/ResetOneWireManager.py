import pyhausbus.HausBusUtils as HausBusUtils

class ResetOneWireManager:
  CLASS_ID = 0
  FUNCTION_ID = 20

  def __init__(self,index:int):
    self.index=index


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return ResetOneWireManager(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"ResetOneWireManager(index={self.index})"

  '''
  @param index 0: loescht alle OneWire Sensor Positionen\r\n1-32: loescht nur den Sensor auf der Position.
  '''
  def getIndex(self):
    return self.index



