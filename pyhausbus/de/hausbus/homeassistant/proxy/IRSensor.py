import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils

class IRSensor(ABusFeature):
  CLASS_ID:int = 33

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return IRSensor(HausBusUtils.getObjectId(deviceId, 33, instanceId))

  """
  """
  def off(self):
    logging.info("off")
    hbCommand = HausBusCommand(self.objectId, 0, "off")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def on(self):
    logging.info("on")
    hbCommand = HausBusCommand(self.objectId, 1, "on")
    hbCommand.send()
    logging.info("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evClicked(self, address:int, command:int):
    logging.info("evClicked"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 202, "evClicked")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOff(self):
    logging.info("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOn(self):
    logging.info("evOn")
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.send()
    logging.info("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evHoldStart(self, address:int, command:int):
    logging.info("evHoldStart"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 203, "evHoldStart")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
    hbCommand.send()
    logging.info("returns")

  """
  @param address IR Adresse.
  @param command IR Kommando.
  """
  def evHoldEnd(self, address:int, command:int):
    logging.info("evHoldEnd"+" address = "+str(address)+" command = "+str(command))
    hbCommand = HausBusCommand(self.objectId, 204, "evHoldEnd")
    hbCommand.addWord(address)
    hbCommand.addWord(command)
    hbCommand.send()
    logging.info("returns")


