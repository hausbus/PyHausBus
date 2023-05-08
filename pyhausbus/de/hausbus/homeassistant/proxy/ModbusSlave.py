import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *

class ModbusSlave(ABusFeature):
  CLASS_ID:int = 14

  def __init__ (self,objectId:int):
    super().__init__(objectId)


