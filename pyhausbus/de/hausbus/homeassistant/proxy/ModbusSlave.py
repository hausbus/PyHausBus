from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils

class ModbusSlave(ABusFeature):
  CLASS_ID:int = 14

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return ModbusSlave(HausBusUtils.getObjectId(deviceId, 14, instanceId))


