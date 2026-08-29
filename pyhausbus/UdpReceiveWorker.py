import socket
import threading
import traceback
from pyhausbus.HausBusUtils import *
from pyhausbus.de.hausbus.homeassistant.proxy import *
import time

BROADCAST_SEND_IP = "192.255.255.255"
BROADCAST_RECEIVE_IP = "0.0.0.0"
BUFFER_SIZE  = 10000

class UdpReceiveWorker:
  UDP_GATEWAY = "#UDP#"

  def __init__(self, func):
    LOGGER.debug("init UdpReceiveWorker")
    self.func = func
    self._running = True
    self._ready = threading.Event()
    self._startup_exception = None
    self._sock = None
    self._thread = None

  def startWorker(self):
    LOGGER.debug("starting udp receive worker")
    self._thread = threading.Thread(target=self.runable, daemon=True)
    self._thread.start()

  def stop(self):
    """Stop the worker.

    Just clearing _running is not enough on its own: recvfrom() below
    blocks until a packet arrives, so the loop would only notice _running
    went False the next time it wakes up. The socket timeout in runable()
    bounds that wait; closing the socket here is a belt-and-suspenders
    attempt to unblock it sooner; but on Linux, closing a socket from a
    different thread does not reliably interrupt another thread's pending
    blocking call on it, so the timeout is what actually guarantees this
    returns.
    """
    LOGGER.debug("stopping udp receive worker")
    self._running = False
    if self._sock is not None:
      try:
        self._sock.close()
      except OSError:
        pass

  def runable(self):
    while self._running:
      try:
        self._sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._sock.bind((BROADCAST_RECEIVE_IP, UDP_PORT))
        # Bounds how long recvfrom() blocks so this thread re-checks
        # _running periodically instead of waiting indefinitely for the
        # next packet (or for stop()'s close() to interrupt it, which is
        # not reliable across threads on Linux - see stop() above).
        self._sock.settimeout(0.5)
        LOGGER.debug("UDP server up and listening")
        self._ready.set()
        
        while self._running:
          try:
            bytesAddressPair = self._sock.recvfrom(BUFFER_SIZE)
          except TimeoutError:
            continue
          message = bytesAddressPair[0]
          address = bytesAddressPair[1]
          LOGGER.debug("Message from Client "+format(address)+": "+bytesToDebugString(message))

          if (len(message) < 15):
            LOGGER.debug(f"message size {len(message)} is too short")
            continue

          if (message[0] != 0xef or message[1] != 0xef):
            LOGGER.debug("invalid header")
            continue

          # 2 = Kontrollbyte 3 = MessageCounter
          offset = [4]
          senderObjectId = bytesToDWord(message, offset)
          LOGGER.debug("senderObjectId = "+str(senderObjectId))

          receiverObjectId = bytesToDWord(message, offset)
          LOGGER.debug("receiverObjectId = "+str(receiverObjectId))

          dataLength = bytesToWord(message, offset)
          if (len(message) < 14 + dataLength):
            LOGGER.debug("message size " + str(len(message)) + " is too short for data length " + str(dataLength) + ": " + bytesToDebugString(message))
            dataLength = len(message) - 14
            # support old incompatible short messages
            # continue
          functionId = bytesToInt(message, offset)
          functionData = message[15:]

          LOGGER.debug("functionId " + str(functionId) + ", functionData " + bytesToDebugString(functionData))

          self.func(senderObjectId, receiverObjectId, functionId, functionData, self.UDP_GATEWAY, False, address[0])
      except (Exception) as err:
        self._startup_exception = err
        self._ready.set()
        
        if not self._running:
          # stop() closed the socket to unblock recvfrom() - exit quietly
          # instead of logging a spurious error and reopening a socket.
          break
        LOGGER.error(err,exc_info=True,stack_info=True)
        time.sleep(5)

    LOGGER.debug("udp receive worker stopped")

  def wait_until_ready(self, timeout: float = 5) -> None:
    if not self._ready.wait(timeout):
        raise TimeoutError("UDP receive worker startup timed out")

    if self._startup_exception:
        raise self._startup_exception