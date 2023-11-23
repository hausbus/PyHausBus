from pyhausbus.HausBusUtils import LOGGER
import time
import threading


class ResultWorker:
  _instance = None
  _resultClass = None
  _resultSenderObjectId = 0
  _resultObject = None
  _condition = threading.Condition()

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

  def _setResultInfo(self, resultClass, resultSenderObjectId:int):
    '''print("resultInfo " + str(resultClass) + ", ID " + str(resultSenderObjectId))'''
    self._resultClass = resultClass
    self._resultSenderObjectId = resultSenderObjectId
    self._resultObject=None

  def waitForResult(self, timeoutInSeconds:int):
    start_time = time.time()
    end_time = start_time + timeoutInSeconds

    with self._condition:
      while self._resultObject == None and time.time() < end_time:
        self._condition.wait(1)

    return self._resultObject

  def waitForEvent(self, event, eventSenderObjectId, timeoutInSeconds:int):
    self._resultClass = event
    self._resultSenderObjectId = eventSenderObjectId
    self._resultObject=None

    start_time = time.time()
    end_time = start_time + timeoutInSeconds

    with self._condition:
      while self._resultObject == None and time.time() < end_time:
        self._condition.wait(1)

    return self._resultObject

  def busDataReceived(self, busDataMessage):
    '''print("got "+str(busDataMessage))'''
    if (self._resultClass != None and busDataMessage.getSenderObjectId()==self._resultSenderObjectId and isinstance(busDataMessage.getData(), self._resultClass)):
      with self._condition:
        self._resultObject = busDataMessage.getData()
        self._condition.notify()
