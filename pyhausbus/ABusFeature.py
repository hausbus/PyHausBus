from pyhausbus.HausBusUtils import LOGGER
from pyhausbus.ObjectId import ObjectId

class ABusFeature:

  def __init__(self, objectId:int):
    self.objectId = objectId
    self.name:str=""

  def getObjectId(self) -> int:
    return self.objectId

  def getName(self) -> str:
    return self.name

  def setName(self, name:str):
      self.name = name

  def __str__(self):
    dummy, classType = str(type(self)).rsplit(".", 1)
    classType = classType[:-2]
    return f"ABusFeature(type={classType}, name={self.name}, objectId={ObjectId(self.objectId)}"
