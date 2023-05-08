import pyhausbus.HausBusUtils as HausBusUtils

class RemoteObjects:
  CLASS_ID = 0
  FUNCTION_ID = 129

  def __init__(self,objectList):
    self.objectList=objectList


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return RemoteObjects(HausBusUtils.bytesToList(dataIn, offset))

  def __str__(self):
    return f"RemoteObjects(objectList={self.objectList})"

  '''
  @param objectList Eine Liste der Verfuegbaren Objekte im Geraete.
  '''
  def getObjectList(self):
    return self.objectList



