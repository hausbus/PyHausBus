import importlib, sys
import socket
import threading
import time
import traceback
import netifaces

from pyhausbus.BusDataMessage import BusDataMessage
from pyhausbus.HausBusUtils import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.UdpReceiveWorker import UdpReceiveWorker
from pyhausbus.de.hausbus.homeassistant.proxy import ProxyFactory
from ipaddress import IPv4Network, IPv4Address


RS485_GATEWAY = "#RS485#"
EVENTS_START = 200
RESULT_START = 128


class BusHandler:

  _singleInstance = None
  sock:None
  listeners = []
  _module_cache = {}
  _receive_worker = None
  broadcastIp: str | None = None
  _discoveryActive: bool = False

  @staticmethod
  def getInstance():
    if BusHandler._singleInstance is None:
      BusHandler._singleInstance = BusHandler()
    return BusHandler._singleInstance

  def __init__(self):
    if BusHandler._singleInstance is None:
      self.broadcastTargets = []
      
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
      self._receive_worker = UdpReceiveWorker(self.busDataReceived)
      self._receive_worker.startWorker()
      self._getBroadcastIp()

  def wait_until_ready(self, timeout: float = 5) -> None:
    self._receive_worker.wait_until_ready(timeout)
    
  def shutdown(self):
    """Stop the receive worker, close the send socket, clear listeners.

    Resets the singleton so a later BusHandler.getInstance() call builds
    a fresh instance (new socket, new receive worker) instead of reusing
    this shut-down one. Safe to call more than once.
    """
    LOGGER.debug("shutting down BusHandler")
    if self._receive_worker is not None:
      self._receive_worker.stop()
    if self.sock is not None:
      try:
        self.sock.close()
      except OSError:
        pass
    self.listeners.clear()
    BusHandler._singleInstance = None

  def fast_import(self, module_name: str):
    if module_name in self._module_cache:
        return self._module_cache[module_name]

    module = importlib.import_module(module_name)
    self._module_cache[module_name] = module
    return module

  def setDiscoveryActive(self, active: bool):
    self._discoveryActive = active
    
  def setBroadcastIp(self, fixedBroadcastIp):
    LOGGER.debug(f"new fixed broadcastIp = {fixedBroadcastIp}")
    self.broadcastIp = fixedBroadcastIp;

  def _getBroadcastIp(self):
    """Collect broadcast addresses of all local interfaces."""

    self.broadcastIps = []
    self.broadcastTargets = []

    try:
        for iface in netifaces.interfaces():
            addresses = netifaces.ifaddresses(iface)

            for address in addresses.get(netifaces.AF_INET, []):
                ip_addr = address.get("addr")
                netmask = address.get("netmask")
                broadcast = address.get("broadcast")

                if not ip_addr or not netmask or not broadcast:
                    continue

                network = IPv4Network(
                    f"{ip_addr}/{netmask}",
                    strict=False,
                )

                self.broadcastTargets.append(
                    {
                        "network": network,
                        "broadcast": broadcast,
                    }
                )

                self.broadcastIps.append(broadcast)

        # Duplikate entfernen
        self.broadcastIps = list(dict.fromkeys(self.broadcastIps))

        if self.broadcastIps:
            self.broadcastIp = self.broadcastIps[0]

        LOGGER.debug(
            "broadcastTargets = %s",
            self.broadcastTargets,
        )

        LOGGER.debug(
            "broadcastIps = %s",
            self.broadcastIps,
        )

    except Exception as err:
        LOGGER.warning(
            "Could not determine broadcast addresses: %s",
            err,
        )

  def busDataReceived(self, senderObjectId, receiverObjectId, functionId, functionData, gateway, corrupted:bool, sender_ip=None):
    # Es kann entweder eine Antwort oder Event des Senders sein oder ein Aufruf auf dem Empfänger
    featureClassId = 0
    identifierId = 0
    if (functionId < RESULT_START):
      featureClassId = getClassId(receiverObjectId)
      identifierId = receiverObjectId
    else:
      featureClassId = getClassId(senderObjectId)
      identifierId = senderObjectId
    
    if self._discoveryActive and sender_ip:
      try:
        sender_address = IPv4Address(sender_ip)

        for target in self.broadcastTargets:
            network = target["network"]
            broadcast = target["broadcast"]

            if sender_address in network:
                self._discoveryActive = False

                if broadcast != self.broadcastIp:
                    LOGGER.debug(
                        "broadcastIp changed from %s to %s",
                        self.broadcastIp,
                        broadcast,
                    )
                    self.broadcastIp = broadcast

                break

      except ValueError:
        LOGGER.debug("Invalid sender IP: %s", sender_ip)

    # fixed lookup table
    className = ProxyFactory.getBusClassNameFor(featureClassId, functionId)
    LOGGER.debug("classId = " + str(featureClassId) + ", functionId = " + str(functionId) + ", className = " + str(className))

    try:
      module_name, class_name = className.rsplit(".", 1)
      module = self.fast_import(className)
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
        LOGGER.error(err, exc_info=True, stack_info=True)

  def sendData(self, data:bytearray, debug:str):

    udpData:bytearray = self.prepareForUDP(data)

    LOGGER.debug(UdpReceiveWorker.UDP_GATEWAY + " COMMAND OUT " + debug)
    LOGGER.debug(UdpReceiveWorker.UDP_GATEWAY + " DATA OUT " + HausBusUtils.formatBytes(udpData))

    targets = (
        self.broadcastIps
        if self._discoveryActive
        else [self.broadcastIp]
    )

    try:
      for target in targets:
        self.sock.sendto(udpData, (target, UDP_PORT))
    except socket.error as e:
      LOGGER.error(e, exc_info=True, stack_info=True)

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
