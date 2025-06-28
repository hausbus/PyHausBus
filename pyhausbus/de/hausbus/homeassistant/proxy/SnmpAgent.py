from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils

class SnmpAgent(ABusFeature):
  CLASS_ID:int = 163

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return SnmpAgent(HausBusUtils.getObjectId(deviceId, 163, instanceId))


