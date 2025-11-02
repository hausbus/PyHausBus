from pyhausbus.BusHandler import BusHandler
from pyhausbus.Templates import Templates
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import (
    RemoteObjects,  
)
from pyhausbus.HausBusUtils import LOGGER
import pyhausbus.de.hausbus.homeassistant.proxy.ProxyFactory as ProxyFactory
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.ABusFeature import ABusFeature
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import EFirmwareId
from pyhausbus.ObjectId import ObjectId
from pyhausbus.Templates import Templates
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Configuration import Configuration
import importlib
import traceback
import time
import threading
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvStarted import EvStarted
from pyhausbus.ResultWorker import ResultWorker

class HomeServer(IBusDataListener):
    _instance = None
    bushandler = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        LOGGER.debug("init homeserver")
        self.bushandler = BusHandler.getInstance()
        self.bushandler.addBusEventListener(ResultWorker())
        self.bushandler.addBusEventListener(self)

    def searchDevices(self):
        controller = Controller(0)
        controller.getModuleId(EIndex.RUNNING)

    def addBusEventListener(self, listener: IBusDataListener):
        self.bushandler.addBusEventListener(listener)

    def removeBusEventListener(self, listener: IBusDataListener):
        self.bushandler.removeBusEventListener(listener)

    def getDeviceInstances(self, senderObjectId: int, remoteObjects: RemoteObjects):
        deviceId = HausBusUtils.getDeviceId(senderObjectId)
        objectList = remoteObjects.getObjectList()

        result = []
        for i in range(0, len(objectList), 2):
            instanceId = objectList[i]
            classId = objectList[i + 1]
            className = ProxyFactory.getBusClassNameForClass(classId)
            objectId = HausBusUtils.getObjectId(deviceId, classId, instanceId)
            
            try:
                module_name, class_name = className.rsplit(".", 1)
                module = importlib.import_module(className)
                cls = getattr(module, class_name)
                obj = cls(objectId)
                result.append(obj)
            except Exception as err:
                LOGGER.error(err,exc_info=True, stack_info=True)
        return result

    def getHomeassistantChannels(self, senderObjectId: int, remoteObjects: RemoteObjects, firmware_id: EFirmwareId, fcke: int):

        instances: list[ABusFeature] = self.getDeviceInstances(senderObjectId, remoteObjects)

        templates = Templates.get_instance()
        
        for instance in instances:
            instanceObjectId = ObjectId(instance.getObjectId())
            name = templates.get_feature_name_from_template(
                firmware_id,
                fcke,
                instanceObjectId.getClassId(),
                instanceObjectId.getInstanceId(),
            )

            LOGGER.debug(
                "name for firmwareId %s, fcke: %s, classId %s, instanceId %s is %s",
                firmware_id,
                fcke,
                instanceObjectId.getClassId(),
                instanceObjectId.getInstanceId(),
                name,
            )

            if name is None:
                className = ProxyFactory.getBusClassNameForClass(
                    instanceObjectId.getClassId()
                ).rsplit(".", 1)[-1]
                name = f"{className} {instanceObjectId.getInstanceId()}"
                LOGGER.debug("generic name %s", name)

            instance.setName(name)
            
        return instances

    def busDataReceived(self, busDataMessage):
        """if a device restarts during runtime, we automatically read moduleId"""
        if isinstance(busDataMessage.getData(), ModuleId):
            LOGGER.debug("auto calling getConfiguration")
            Controller(busDataMessage.getSenderObjectId()).getConfiguration()
            

        if isinstance(busDataMessage.getData(), Configuration):
            LOGGER.debug("auto calling getRemoteObjects")
            Controller(busDataMessage.getSenderObjectId()).getRemoteObjects()

        """ if a device restarts during runtime, we automatically read moduleId"""
        if isinstance(busDataMessage.getData(), EvStarted):
            LOGGER.debug("auto calling getModuleId")
            Controller(busDataMessage.getSenderObjectId()).getModuleId(EIndex.RUNNING)
