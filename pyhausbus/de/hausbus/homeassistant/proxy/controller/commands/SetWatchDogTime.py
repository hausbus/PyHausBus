import pyhausbus.HausBusUtils as HausBusUtils

class SetWatchDogTime:
  CLASS_ID = 0
  FUNCTION_ID = 21

  def __init__(self,time:int):
    self.time=time


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetWatchDogTime(HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"SetWatchDogTime(time={self.time})"

  '''
  @param time Zeit in Sekunden bis zum Reset wenn kein Ping empfangen wird. 0 deativiert den WatchDog.
  '''
  def getTime(self):
    return self.time



