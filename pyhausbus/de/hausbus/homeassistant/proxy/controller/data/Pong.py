import pyhausbus.HausBusUtils as HausBusUtils

class Pong:
  CLASS_ID = 0
  FUNCTION_ID = 199

  def __init__(self,watchDogTime:int):
    self.watchDogTime=watchDogTime


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Pong(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"Pong(watchDogTime={self.watchDogTime})"

  '''
  @param watchDogTime Verbleibende Zeit in Sekunden bis zum Watchdog Reset.
  '''
  def getWatchDogTime(self):
    return self.watchDogTime



