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

  def startWorker(self):
    LOGGER.debug("starting udp receive worker")
    t = threading.Thread(target=self.runable)
    t.start()

  def runable(self):
    while(True):
      try:
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        UDPServerSocket.bind((BROADCAST_RECEIVE_IP, UDP_PORT))
        LOGGER.debug("UDP server up and listening")

        while(True):
          bytesAddressPair = UDPServerSocket.recvfrom(BUFFER_SIZE)
          message = bytesAddressPair[0]
          address = bytesAddressPair[1]
          LOGGER.debug("Message from Client "+format(address)+": "+bytesToDebugString(message))


          if (len(message) == 0):
            LOGGER.debug("got empty message")
            continue

          if (message[0] != 0xef | message[1] != 0xef):
            LOGGER.debug("invalid header")
            continue

          if (len(message) < 15):
            LOGGER.debug("message size " + len(message) + " is too short")
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
            # continue
          functionId = bytesToInt(message, offset)
          functionData = message[15:]

          LOGGER.debug("functionId " + str(functionId) + ", functionData " + bytesToDebugString(functionData))

          self.func(senderObjectId, receiverObjectId, functionId, functionData, self.UDP_GATEWAY, False)
      except (Exception) as err:
        LOGGER.error(err,exc_info=True,stack_info=True)
        time.sleep(5)
