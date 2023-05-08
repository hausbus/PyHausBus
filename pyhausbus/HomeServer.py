import logging
from BusHandler import BusHandler
from IBusDataListener import IBusDataListener
from de.hausbus.homeassistant.proxy.Controller import Controller
from de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import RemoteObjects
import de.hausbus.homeassistant.proxy.ProxyFactory
import HausBusUtils
import importlib
import traceback

class HomeServer: 
  bushandler=None
  
  def __init__(self):
    logging.info("init")
    self.bushandler = BusHandler.getInstance()

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
      className = de.hausbus.homeassistant.proxy.ProxyFactory.getBusClassNameForClass(classId);
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
