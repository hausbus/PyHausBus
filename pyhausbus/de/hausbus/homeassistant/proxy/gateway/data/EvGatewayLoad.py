import pyhausbus.HausBusUtils as HausBusUtils

class EvGatewayLoad:
  CLASS_ID = 176
  FUNCTION_ID = 200

  def __init__(self,messagesPerMinute:int, bytesPerMinute:int):
    self.messagesPerMinute=messagesPerMinute
    self.bytesPerMinute=bytesPerMinute


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvGatewayLoad(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset))

  def __str__(self):
    return f"EvGatewayLoad(messagesPerMinute={self.messagesPerMinute}, bytesPerMinute={self.bytesPerMinute})"

  '''
  @param messagesPerMinute Anzahl der Nachrichten pro Sekunde.
  '''
  def getMessagesPerMinute(self):
    return self.messagesPerMinute

  '''
  @param bytesPerMinute Anzahl der Datenbytes pro Sekunde.
  '''
  def getBytesPerMinute(self):
    return self.bytesPerMinute



