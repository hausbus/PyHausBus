from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFeatureId import EFeatureId
import pyhausbus.HausBusUtils as HausBusUtils

class EnableFeature:
  CLASS_ID = 0
  FUNCTION_ID = 19

  def __init__(self,featureId:EFeatureId, key:str):
    self.featureId=featureId
    self.key=key


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EnableFeature(EFeatureId._fromBytes(dataIn, offset), HausBusUtils.bytesToString(dataIn, offset))

  def __str__(self):
    return f"EnableFeature(featureId={self.featureId}, key={self.key})"

  '''
  @param featureId Zusatzfunktion.
  '''
  def getFeatureId(self):
    return self.featureId

  '''
  @param key Der Schluessel mit dem die Zusatzfunktion aktiviert werden soll..
  '''
  def getKey(self):
    return self.key



