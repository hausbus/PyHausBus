import pyhausbus.HausBusUtils as HausBusUtils

class ObjectId:
  objectId:int=0

  def __init__ (self, objectId:int):
    self.objectId = objectId

  def getValue(self) -> int:
    return self.objectId

  def getDeviceId(self) -> int:
    return HausBusUtils.getDeviceId(self.objectId)

  def getClassId(self) -> int:
    return HausBusUtils.getClassId(self.objectId)

  def getInstanceId(self) -> int:
    return HausBusUtils.getInstanceId(self.objectId)

  def __str__(self):
    return f"Object(DeviceId={self.getDeviceId()}, ClassId={self.getClassId()}, InstanceId={self.getInstanceId()} - {hex(self.objectId)} ({self.objectId}))"
