import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.led.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.led.params.MOptions import MOptions
from pyhausbus.de.hausbus.homeassistant.proxy.led.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.led.data.MinBrightness import MinBrightness

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
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

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
    ResultWorker()._setResultInfo(None,self.getObjectId())
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

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
    ResultWorker()._setResultInfo(None,self.getObjectId())
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOff(self):
    logging.info("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    ResultWorker()._setResultInfo(None,self.getObjectId())
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evBlink(self):
    logging.info("evBlink")
    hbCommand = HausBusCommand(self.objectId, 202, "evBlink")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:int):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def off(self, offDelay:int):
    logging.info("off"+" offDelay = "+str(offDelay))
    hbCommand = HausBusCommand(self.objectId, 2, "off")
    hbCommand.addWord(offDelay)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  """
  def setMinBrightness(self, minBrightness:int):
    logging.info("setMinBrightness"+" minBrightness = "+str(minBrightness))
    hbCommand = HausBusCommand(self.objectId, 6, "setMinBrightness")
    hbCommand.addByte(minBrightness)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param cmdDelay Dauer Wert * Zeitbasis [ms].
  """
  def evCmdDelay(self, cmdDelay:int):
    logging.info("evCmdDelay"+" cmdDelay = "+str(cmdDelay))
    hbCommand = HausBusCommand(self.objectId, 203, "evCmdDelay")
    hbCommand.addWord(cmdDelay)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getMinBrightness(self):
    logging.info("getMinBrightness")
    hbCommand = HausBusCommand(self.objectId, 7, "getMinBrightness")
    ResultWorker()._setResultInfo(MinBrightness,self.getObjectId())
    hbCommand.send()
    logging.info("returns")

  """
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  """
  def MinBrightness(self, minBrightness:int):
    logging.info("MinBrightness"+" minBrightness = "+str(minBrightness))
    hbCommand = HausBusCommand(self.objectId, 130, "MinBrightness")
    hbCommand.addByte(minBrightness)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    logging.info("returns")


