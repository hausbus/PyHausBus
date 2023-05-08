import pyhausbus.HausBusUtils as HausBusUtils

class SetUnitGroupState:
  CLASS_ID = 0
  FUNCTION_ID = 14

  def __init__(self,index:int, member:int, state:int, triggerBits:int):
    self.index=index
    self.member=member
    self.state=state
    self.triggerBits=triggerBits


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetUnitGroupState(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetUnitGroupState(index={self.index}, member={self.member}, state={self.state}, triggerBits={self.triggerBits})"

  '''
  @param index Gruppenindex.
  '''
  def getIndex(self):
    return self.index

  '''
  @param member Gruppenteilnehmer 0-15.
  '''
  def getMember(self):
    return self.member

  '''
  @param state Zustand des Teilnehmers 0=AUS.
  '''
  def getState(self):
    return self.state

  '''
  @param triggerBits Anzahl der Teilnehmer die gesetzt sein muessen damit evGroupOn erzeugt wird.
  '''
  def getTriggerBits(self):
    return self.triggerBits



