import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.EStatus import EStatus
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.MEventMask import MEventMask
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.MOptionMask import MOptionMask
from pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.params.MOptions import MOptions

class LogicalButton(ABusFeature):
  CLASS_ID:int = 20

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return LogicalButton(HausBusUtils.getObjectId(deviceId, 20, instanceId))

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
  @param button1 instanzId des 1.Tasters.
  @param button2 instanzId des 2.Tasters.
  @param button3 .
  @param button4 .
  @param button5 .
  @param button6 .
  @param button7 .
  @param button8 .
  @param led1 .
  @param led2 .
  @param led3 .
  @param led4 .
  @param led5 .
  @param led6 .
  @param led7 .
  @param led8 .
  """
  def setConfiguration(self, button1:int, button2:int, button3:int, button4:int, button5:int, button6:int, button7:int, button8:int, led1:int, led2:int, led3:int, led4:int, led5:int, led6:int, led7:int, led8:int):
    logging.info("setConfiguration"+" button1 = "+str(button1)+" button2 = "+str(button2)+" button3 = "+str(button3)+" button4 = "+str(button4)+" button5 = "+str(button5)+" button6 = "+str(button6)+" button7 = "+str(button7)+" button8 = "+str(button8)+" led1 = "+str(led1)+" led2 = "+str(led2)+" led3 = "+str(led3)+" led4 = "+str(led4)+" led5 = "+str(led5)+" led6 = "+str(led6)+" led7 = "+str(led7)+" led8 = "+str(led8))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(button1)
    hbCommand.addByte(button2)
    hbCommand.addByte(button3)
    hbCommand.addByte(button4)
    hbCommand.addByte(button5)
    hbCommand.addByte(button6)
    hbCommand.addByte(button7)
    hbCommand.addByte(button8)
    hbCommand.addByte(led1)
    hbCommand.addByte(led2)
    hbCommand.addByte(led3)
    hbCommand.addByte(led4)
    hbCommand.addByte(led5)
    hbCommand.addByte(led6)
    hbCommand.addByte(led7)
    hbCommand.addByte(led8)
    hbCommand.send()
    logging.info("returns")

  """
  @param button1 .
  @param button2 .
  @param button3 .
  @param button4 .
  @param button5 .
  @param button6 .
  @param button7 .
  @param button8 .
  @param led1 .
  @param led2 .
  @param led3 .
  @param led4 .
  @param led5 .
  @param led6 .
  @param led7 .
  @param led8 .
  """
  def Configuration(self, button1:int, button2:int, button3:int, button4:int, button5:int, button6:int, button7:int, button8:int, led1:int, led2:int, led3:int, led4:int, led5:int, led6:int, led7:int, led8:int):
    logging.info("Configuration"+" button1 = "+str(button1)+" button2 = "+str(button2)+" button3 = "+str(button3)+" button4 = "+str(button4)+" button5 = "+str(button5)+" button6 = "+str(button6)+" button7 = "+str(button7)+" button8 = "+str(button8)+" led1 = "+str(led1)+" led2 = "+str(led2)+" led3 = "+str(led3)+" led4 = "+str(led4)+" led5 = "+str(led5)+" led6 = "+str(led6)+" led7 = "+str(led7)+" led8 = "+str(led8))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(button1)
    hbCommand.addByte(button2)
    hbCommand.addByte(button3)
    hbCommand.addByte(button4)
    hbCommand.addByte(button5)
    hbCommand.addByte(button6)
    hbCommand.addByte(button7)
    hbCommand.addByte(button8)
    hbCommand.addByte(led1)
    hbCommand.addByte(led2)
    hbCommand.addByte(led3)
    hbCommand.addByte(led4)
    hbCommand.addByte(led5)
    hbCommand.addByte(led6)
    hbCommand.addByte(led7)
    hbCommand.addByte(led8)
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
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
  """
  def evOn(self, brightness:int):
    logging.info("evOn"+" brightness = "+str(brightness))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addByte(brightness)
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
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def off(self, offDelay:int):
    logging.info("off"+" offDelay = "+str(offDelay))
    hbCommand = HausBusCommand(self.objectId, 2, "off")
    hbCommand.addWord(offDelay)
    hbCommand.send()
    logging.info("returns")

  """
  @param brightness 0-100% Helligkeit.
  @param duration Einschaltdauer in Sekunden.
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
  @param offTime a 100ms.
  @param onTime a 100ms.
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
  @param status Zustand der Taster LEDs.
  """
  def Status(self, status:EStatus):
    logging.info("Status"+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(status.value)
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
  @param holdTimeout Zeit a 10ms.
  @param waitForDoubleClickTimeout Zeit a 10ms.
  @param eventMask Jedes gesetzte Bit aktiviert das Melden des entsprechenden Events..
  @param optionMask 0: invertiert die Eingangslogik\r\n1: setzt den Initialzustand auf 0.
  """
  def setButtonConfiguration(self, holdTimeout:int, waitForDoubleClickTimeout:int, eventMask:MEventMask, optionMask:MOptionMask):
    logging.info("setButtonConfiguration"+" holdTimeout = "+str(holdTimeout)+" waitForDoubleClickTimeout = "+str(waitForDoubleClickTimeout)+" eventMask = "+str(eventMask)+" optionMask = "+str(optionMask))
    hbCommand = HausBusCommand(self.objectId, 11, "setButtonConfiguration")
    hbCommand.addByte(holdTimeout)
    hbCommand.addByte(waitForDoubleClickTimeout)
    hbCommand.addByte(eventMask.getValue())
    hbCommand.addByte(optionMask.getValue())
    hbCommand.send()
    logging.info("returns")

  """
  @param dimmOffset 0-100% offset auf den im Kommando angegebenen Helligkeitswert.
  @param minBrightness Eine ausgeschaltete LED leuchtet immer noch mit dieser Helligkeit 0-100%.
  @param timeBase Zeitbasis [ms] fuer Zeitabhaengige Befehle..
  @param options eservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standard-Einstellungen..
  """
  def setLedConfiguration(self, dimmOffset:int, minBrightness:int, timeBase:int, options:MOptions):
    logging.info("setLedConfiguration"+" dimmOffset = "+str(dimmOffset)+" minBrightness = "+str(minBrightness)+" timeBase = "+str(timeBase)+" options = "+str(options))
    hbCommand = HausBusCommand(self.objectId, 12, "setLedConfiguration")
    hbCommand.addByte(dimmOffset)
    hbCommand.addByte(minBrightness)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
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
  """
  def getMinBrightness(self):
    logging.info("getMinBrightness")
    hbCommand = HausBusCommand(self.objectId, 7, "getMinBrightness")
    hbCommand.send()
    logging.info("returns")


