import logging
from pyhausbus.BusHandler import BusHandler
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import RemoteObjects
import pyhausbus.de.hausbus.homeassistant.proxy.ProxyFactory as ProxyFactory
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
import importlib
import traceback
import time
import threading
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvStarted import EvStarted


class HomeServer: 
  bushandler=None
  
  def __init__(self):
    logging.info("init")
    self.bushandler = BusHandler.getInstance()
    self.resultClass=None
    self.resultSenderObjectId=0
    self.resultObject=None
    self.bushandler.addBusEventListener(self)
    self.condition = threading.Condition()

    
  def searchDevices(self):
    controler = Controller(0)
    controler.getModuleId(EIndex.RUNNING)
    
  def addBusEventListener(self, listener:IBusDataListener):
    self.bushandler.addBusEventListener(listener)

  def removeBusEventListener(self, listener:IBusDataListener):
    self.bushandler.removeBusEventListener(listener)
    
  
  def getDeviceInstances(self, senderObjectId: int, remoteObjects: RemoteObjects):
    deviceId = HausBusUtils.getDeviceId(senderObjectId)
    objectList = remoteObjects.getObjectList()
    
    result=[]
    for i in range (0, len(objectList),2):
      instanceId = objectList[i]
      classId = objectList[i+1];
      className = ProxyFactory.getBusClassNameForClass(classId);
      objectId = HausBusUtils.getObjectId(deviceId, classId, instanceId)
        
      try:
        module_name, class_name = className.rsplit(".", 1)
        module = importlib.import_module(className)
        cls = getattr(module, class_name)
        obj = cls(objectId)
        result.append(obj)
      except (Exception) as err:
        print("error:", err)
        traceback.print_exc()
    return result

  def setResultInfo(self, resultClass, resultSenderObjectId:int):
    self.resultClass = resultClass
    self.resultSenderObjectId=resultSenderObjectId
  
  def waitForResult(self, timeoutInSeconds:int):
    start_time = time.time()
    end_time = start_time + timeoutInSeconds
    
    with self.condition:
      while self.resultObject==None and time.time() < end_time:
        self.condition.wait(1)
      
    return self.resultObject
  
  def busDataReceived(self, busDataMessage):

    ''' if we receive a ModuleId from a device we automatically ask for the remote objects'''
    if (isinstance(busDataMessage.getData(), ModuleId)):
      Controller(busDataMessage.getSenderObjectId()).getRemoteObjects()
    
    ''' if a device restarts during runtime, we automatically read moduleId'''
    if (isinstance(busDataMessage.getData(), EvStarted)):
      Controller(busDataMessage.getSenderObjectId()).getModuleId()

    if (self.resultClass!=None and isinstance(busDataMessage.getData(), self.resultClass)):
      with self.condition:
        self.resultObject = busDataMessage.getData()
        self.condition.notify()
        
