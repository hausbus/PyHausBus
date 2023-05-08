import pyhausbus.HausBusUtils as HausBusUtils

class TimeDifference:
  CLASS_ID = 0
  FUNCTION_ID = 197

  def __init__(self,timeDifference:int):
    self.timeDifference=timeDifference


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return TimeDifference(HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"TimeDifference(timeDifference={self.timeDifference})"

  '''
  @param timeDifference Abweichung der internen Wochenzeit in Minuten Achtung: Vorzeichenbehaftetes Byte. 255 entspricht -1.
  '''
  def getTimeDifference(self):
    return self.timeDifference



