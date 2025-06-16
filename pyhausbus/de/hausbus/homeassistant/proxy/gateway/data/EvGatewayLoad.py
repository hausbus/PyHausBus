import pyhausbus.HausBusUtils as HausBusUtils

class EvGatewayLoad:
  CLASS_ID = 176
  FUNCTION_ID = 200

  def __init__(self,inMessagesPerMinute:int, outMessagesPerMinute:int, inBytesPerMinute:int, outBytesPerMinute:int, messageQueueHighWater:int):
    self.inMessagesPerMinute=inMessagesPerMinute
    self.outMessagesPerMinute=outMessagesPerMinute
    self.inBytesPerMinute=inBytesPerMinute
    self.outBytesPerMinute=outBytesPerMinute
    self.messageQueueHighWater=messageQueueHighWater


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvGatewayLoad(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"EvGatewayLoad(inMessagesPerMinute={self.inMessagesPerMinute}, outMessagesPerMinute={self.outMessagesPerMinute}, inBytesPerMinute={self.inBytesPerMinute}, outBytesPerMinute={self.outBytesPerMinute}, messageQueueHighWater={self.messageQueueHighWater})"

  '''
  @param inMessagesPerMinute Anzahl der eingehenden Nachrichten pro Minute.
  '''
  def getInMessagesPerMinute(self):
    return self.inMessagesPerMinute

  '''
  @param outMessagesPerMinute Anzahl der ausgehenden Nachrichten pro Minute.
  '''
  def getOutMessagesPerMinute(self):
    return self.outMessagesPerMinute

  '''
  @param inBytesPerMinute Anzahl der Datenbytes von eingehenden Nachrichten pro Minute.
  '''
  def getInBytesPerMinute(self):
    return self.inBytesPerMinute

  '''
  @param outBytesPerMinute Anzahl der Datenbytes von ausgehenden Nachrichten pro Minute.
  '''
  def getOutBytesPerMinute(self):
    return self.outBytesPerMinute

  '''
  @param messageQueueHighWater Maximale Anzahl von Nachrichten in der Warteschlange innerhalb der letzten Minute.
  '''
  def getMessageQueueHighWater(self):
    return self.messageQueueHighWater



