import threading
from pyhausbus.de.hausbus.homeassistant.proxy import ProxyFactory
from pyhausbus.HausBusUtils import *
from pyhausbus.BusDataMessage import BusDataMessage
from pyhausbus.IBusDataListener import IBusDataListener
import time
import importlib
from pyhausbus.UdpReceiveWorker import UdpReceiveWorker
import socket
import pyhausbus.HausBusUtils as HausBusUtils
import traceback

RS485_GATEWAY = "#RS485#"
EVENTS_START = 200
RESULT_START = 128

class BusHandler:

  _singleInstance = None
  sock:None
  broadcastIp = "192.168.178.255"
  listeners = []

  @staticmethod
  def getInstance():
    if BusHandler._singleInstance is None:
      BusHandler._singleInstance = BusHandler()
    return BusHandler._singleInstance

  def __init__(self):
    if BusHandler._singleInstance is None:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
      x = UdpReceiveWorker(self.busDataReceived)
      x.startWorker()
      self._getBroadcastIp()

  def _getBroadcastIp(self):
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        temp_socket.connect(("8.8.8.8", 80))
        own_ip = temp_socket.getsockname()[0].split('.')
        self.broadcastIp = own_ip[0] + "." + own_ip[1] + "." + own_ip[2] + ".255"
    finally:
        temp_socket.close()

  def busDataReceived(self, senderObjectId, receiverObjectId, functionId, functionData, gateway, corrupted:bool):
    # Es kann entweder eine Antwort oder Event des Senders sein oder ein Aufruf auf dem Empfänger
    featureClassId = 0
    identifierId = 0
    if (functionId < RESULT_START):
      featureClassId = getClassId(receiverObjectId)
      identifierId = receiverObjectId
    else:
      featureClassId = getClassId(senderObjectId)
      identifierId = senderObjectId

    LOGGER.debug("classId = " + str(featureClassId) + ", functionId = " + str(functionId))
    className = ProxyFactory.getBusClassNameFor(featureClassId, functionId)
    if (className=="de.hausbus.proxy.LogicalButton"):
      LOGGER.debug("test")

    try:
      module_name, class_name = className.rsplit(".", 1)
      module = importlib.import_module(className)
      cls = getattr(module, class_name)
      method = getattr(cls, "_fromBytes")
      offset = [0]
      newObject = method(functionData, offset)

      add = ""
      if (corrupted):
        add = " (corrupted) "

      message = gateway + " COMMAND IN " + add + " from " + str(getDeviceId(senderObjectId)) + " to " + str(getDeviceId(receiverObjectId)) + ": " + str(newObject) + ", Sender: " + formatObjectId(senderObjectId) + ", Receiver: " + str(formatObjectId(receiverObjectId))
      LOGGER.debug(message)

      if (not corrupted):
        newMessage = BusDataMessage(senderObjectId, receiverObjectId, newObject)
        LOGGER.debug("got: " + str(newObject) + " from " + str(senderObjectId) + " to " + str(receiverObjectId))
        for actListener in self.listeners:
          actListener.busDataReceived(newMessage)
    except (Exception, RuntimeError, TypeError, NameError, OSError) as err:
        LOGGER.error(err,exc_info=True,stack_info=True)

  def sendData(self, data:bytearray, debug:str):

    udpData:bytearray = self.prepareForUDP(data)

    LOGGER.debug(UdpReceiveWorker.UDP_GATEWAY + " COMMAND OUT " + debug)
    LOGGER.debug(UdpReceiveWorker.UDP_GATEWAY + " DATA OUT " + HausBusUtils.formatBytes(udpData))

    try:
      self.sock.sendto(udpData, (self.broadcastIp, UDP_PORT))
    except socket.error as e:
      LOGGER.error(e,exc_info=True,stack_info=True)

  def prepareForUDP(self, data:bytearray) -> bytearray:
    result = bytearray(len(data) + 2)
    result[0] = 0xef
    result[1] = 0xef
    result[2:] = data[:]
    return result

  def addBusEventListener(self, listener:IBusDataListener):
    if not listener in self.listeners:
      self.listeners.append(listener)

  def removeBusEventListener(self, listener:IBusDataListener):
    self.listeners.remove(listener)
