import pyhausbus.HausBusUtils as HausBusUtils

class EvSignal:
  CLASS_ID = 90
  FUNCTION_ID = 200

  def __init__(self,time:int, signalCount:int, power:int, signalDuration:int):
    self.time=time
    self.signalCount=signalCount
    self.power=power
    self.signalDuration=signalDuration


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvSignal(HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"EvSignal(time={self.time}, signalCount={self.signalCount}, power={self.power}, signalDuration={self.signalDuration})"

  '''
  @param time Systemzeit des ESP zu Debugzwecken.
  '''
  def getTime(self):
    return self.time

  '''
  @param signalCount Anzahl gez?hlter S0 Signale seit dem letzten Zur?cksetzen.
  '''
  def getSignalCount(self):
    return self.signalCount

  '''
  @param power Aktuelle Leistung in Watt.
  '''
  def getPower(self):
    return self.power

  '''
  @param signalDuration Dauer des gemessenen S0 Signals in ms.
  '''
  def getSignalDuration(self):
    return self.signalDuration



