import pyhausbus.HausBusUtils as HausBusUtils

class EvToggleByDuty:
  CLASS_ID = 19
  FUNCTION_ID = 205

  def __init__(self,duty:int, durationSeconds:int):
    self.duty=duty
    self.durationSeconds=durationSeconds


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvToggleByDuty(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvToggleByDuty(duty={self.duty}, durationSeconds={self.durationSeconds})"

  '''
  @param duty 0-100% Pulsverh?ltnis.
  '''
  def getDuty(self):
    return self.duty

  '''
  @param durationSeconds Einschaltdauer in Sekunden.
  '''
  def getDurationSeconds(self):
    return self.durationSeconds



