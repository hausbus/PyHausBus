from pyhausbus.BusHandler import BusHandler
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import (
    RemoteObjects,
)
from pyhausbus.HausBusUtils import LOGGER
import pyhausbus.de.hausbus.homeassistant.proxy.ProxyFactory as ProxyFactory
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
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
        controler = Controller(0)
        controler.getModuleId(EIndex.RUNNING)

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

    def busDataReceived(self, busDataMessage):
        """if a device restarts during runtime, we automatically read moduleId"""
        if isinstance(busDataMessage.getData(), EvStarted):
            Controller(busDataMessage.getSenderObjectId()).getModuleId(EIndex.RUNNING)
