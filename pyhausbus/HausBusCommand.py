from pyhausbus.BusHandler import BusHandler
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.HausBusUtils import LOGGER
from pyhausbus.ObjectId import ObjectId

class HausBusCommand:

  def __init__ (self, receiverObjectId:int, functionId:int, debug:str):
    self.commandCounter:int = 0
    self.receiverObjectId = receiverObjectId
    self.debug = debug
    self.busHandler = BusHandler.getInstance()
    self.data:bytearray=bytearray()
    self.params:bytearray=bytearray()
    self.bytes:bytearray=None

    # Kontroll-Byte
    self.data.append(0)

    # Nachrichtenzaehler
    self.data.append(0)

    # Sender-ID
    for act in HausBusUtils.dWordToBytes(HausBusUtils.HOMESERVER_OBJECT_ID):
      self.data.append(act)

    # Empfaenger-ID
    for act in HausBusUtils.dWordToBytes(receiverObjectId):
      self.data.append(act)

    self.params.append(functionId)

  def addByte(self, byteParam:int):
    self.params.append(byteParam)

  def addSByte(self, sByteParam:int):
    if (sByteParam < 0):
      self.params.append((256 + sByteParam))
    else:
      self.params.append(sByteParam)

  def addBlob(self, blob:bytearray):
    for act in blob:
      self.params.append(act)

  def addString(self, value:str):
    for i in range(len(value)):
      self.params.append(value[i])
    self.params.append(0)

  def addMap(self, inMap):
    for key, value in inMap.items():
      self.addByte(key)
      self.addByte(value)

  def addWord(self, wordParam:int):
    HausBusUtils.addWord(wordParam, self.params)

  def addDWord(self, dWordParam:int):
    HausBusUtils.addDword(dWordParam, self.params)

  def _createBytes(self):

    # Datenlaenge
    for act in HausBusUtils.wordToBytes(len(self.params)):
      self.data.append(act)

    # Daten
    for act in self.params:
      self.data.append(act)

    self.bytes = bytearray(len(self.data))
    for i in range (len(self.data)):
      self.bytes[i] = self.data[i]

  def send(self):
    LOGGER.debug("Sende " + self.debug + " an " + str(ObjectId(self.receiverObjectId)))
    if (self.bytes == None):
      self._createBytes()

    return self.busHandler.sendData(self.bytes, self.debug + " to " + str(HausBusUtils.getDeviceId(self.receiverObjectId)))

  def __str__(self):
    return f"HausBusCommand(debug={self.debug} to {HausBusUtils.formatObjectId(self.receiverObjectId)}, params={self.params}, data={self.data}"