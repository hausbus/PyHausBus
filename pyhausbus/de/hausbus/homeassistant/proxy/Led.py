import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.led.params.MOptions import MOptions

class Led(ABusFeature):
  CLASS_ID:int = 21

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Led(HausBusUtils.getObjectId(deviceId, 21, instanceId))

  """
  """
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param dimmOffset 0-100% offset auf den im Kommando angegebenen Helligkeitswert.
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  @param timeBase Zeitbasis [ms] fuer Zeitabhaengige Befehle..
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  """
  def setConfiguration(self, dimmOffset:int, minBrightness:int, timeBase:int, options:MOptions):
    logging.info("setConfiguration"+" dimmOffset = "+str(dimmOffset)+" minBrightness = "+str(minBrightness)+" timeBase = "+str(timeBase)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(dimmOffset)
    hbCommand.addByte(minBrightness)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param brightness 0-100% Helligkeit.
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  @param onDelay Einschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def on(self, brightness:int, duration:int, onDelay:int):
    logging.info("on"+" brightness = "+str(brightness)+" duration = "+str(duration)+" onDelay = "+str(onDelay))
    hbCommand = HausBusCommand(self.objectId, 3, "on")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
    hbCommand.addWord(onDelay)
    hbCommand.send()
    logging.info("returns")

  """
  @param brightness 0-100% Helligkeit.
  @param offTime Ausschaltdauer: \r\nWert * Zeitbasis [ms].
  @param onTime Einschaltdauer: \r\nWert * Zeitbasis [ms].
  @param quantity Anzahl Blinks.
  """
  def blink(self, brightness:int, offTime:int, onTime:int, quantity:int):
    logging.info("blink"+" brightness = "+str(brightness)+" offTime = "+str(offTime)+" onTime = "+str(onTime)+" quantity = "+str(quantity))
    hbCommand = HausBusCommand(self.objectId, 4, "blink")
    hbCommand.addByte(brightness)
    hbCommand.addByte(offTime)
    hbCommand.addByte(onTime)
    hbCommand.addByte(quantity)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param dimmOffset 0-100% offset auf den im Kommando angegebenen Helligkeitswert.
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  @param timeBase Zeitbasis [ms] f?  ? ? ?r Zeitabh?  ? ? ??ngige Befehle..
  @param options Reservierte Bits m?  ? ? ?ssen immer deaktiviert sein. Das Aktivieren eines reservierten Bits f?  ? ? ?hrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  """
  def Configuration(self, dimmOffset:int, minBrightness:int, timeBase:int, options:MOptions):
    logging.info("Configuration"+" dimmOffset = "+str(dimmOffset)+" minBrightness = "+str(minBrightness)+" timeBase = "+str(timeBase)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(dimmOffset)
    hbCommand.addByte(minBrightness)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param brightness Helligkeit der LED.
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  """
  def Status(self, brightness:int, duration:int):
    logging.info("Status"+" brightness = "+str(brightness)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
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
  @param brightness 0-100% Helligkeit.
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  """
  def evOn(self, brightness:int, duration:int):
    logging.info("evOn"+" brightness = "+str(brightness)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addByte(brightness)
    hbCommand.addWord(duration)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evBlink(self):
    logging.info("evBlink")
    hbCommand = HausBusCommand(self.objectId, 202, "evBlink")
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:int):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode)
    hbCommand.send()
    logging.info("returns")

  """
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def off(self, offDelay:int):
    logging.info("off"+" offDelay = "+str(offDelay))
    hbCommand = HausBusCommand(self.objectId, 2, "off")
    hbCommand.addWord(offDelay)
    hbCommand.send()
    logging.info("returns")

  """
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  """
  def setMinBrightness(self, minBrightness:int):
    logging.info("setMinBrightness"+" minBrightness = "+str(minBrightness))
    hbCommand = HausBusCommand(self.objectId, 6, "setMinBrightness")
    hbCommand.addByte(minBrightness)
    hbCommand.send()
    logging.info("returns")

  """
  @param cmdDelay Dauer Wert * Zeitbasis [ms].
  """
  def evCmdDelay(self, cmdDelay:int):
    logging.info("evCmdDelay"+" cmdDelay = "+str(cmdDelay))
    hbCommand = HausBusCommand(self.objectId, 203, "evCmdDelay")
    hbCommand.addWord(cmdDelay)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getMinBrightness(self):
    logging.info("getMinBrightness")
    hbCommand = HausBusCommand(self.objectId, 7, "getMinBrightness")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  """
  def MinBrightness(self, minBrightness:int):
    logging.info("MinBrightness"+" minBrightness = "+str(minBrightness))
    hbCommand = HausBusCommand(self.objectId, 130, "MinBrightness")
    hbCommand.addByte(minBrightness)
    hbCommand.send()
    logging.info("returns")


