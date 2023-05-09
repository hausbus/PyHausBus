import pyhausbus.HausBusUtils as HausBusUtils


class BusDataMessage:

  def __init__(self, senderObjectId, receiverObjectId, data):
    self.senderObjectId = senderObjectId
    self.receiverObjectId = receiverObjectId
    self.data = data
    self.time = HausBusUtils.getClockIndependMillis()

  def getSenderObjectId(self):
    return self.senderObjectId

  def getReceiverObjectId(self):
    return self.receiverObjectId

  def getData(self):
    return self.data

  def __str__(self):
    return f"BusMessage(senderObjectId={self.senderObjectId}, receiverObjectId={self.receiverObjectId}, data={self.data})"

