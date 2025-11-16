import importlib

from pyhausbus.ABusFeature import ABusFeature
from pyhausbus.BusHandler import BusHandler
from pyhausbus.HausBusUtils import HOMESERVER_DEVICE_ID
from pyhausbus.HausBusUtils import LOGGER
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.IBusDeviceListener import IBusDeviceListener
from pyhausbus.ObjectId import ObjectId
from pyhausbus.ResultWorker import ResultWorker
from pyhausbus.Templates import Templates
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
import pyhausbus.de.hausbus.homeassistant.proxy.ProxyFactory as ProxyFactory
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvStarted import EvStarted
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import  RemoteObjects
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EIndex import EIndex
import threading
import queue
import time
import logging
import traceback

_module_cache = {}
_class_cache = {}


class HomeServer(IBusDataListener):
    _instance = None
    bushandler = None
    device_listeners = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        LOGGER.debug("init homeserver")
        self.bushandler = BusHandler.getInstance()
        self.bushandler.addBusEventListener(ResultWorker())
        self.bushandler.addBusEventListener(self)
        self._receivedSomething = False
        self.module_ids: dict[int, ModuleId] = {}
        self.configurations: dict[int, Configuration] = {}
        self.remote_objects: dict[int, RemoteObjects] = {}
        self.worker = DeviceWorker(self)
        self.worker.start()
        self.collector = DeviceCollector(self.worker, timeout=1.0)
        self.collector.start()
        self.known_devices = set()

    def searchDevices(self):
        controller = Controller(0)
        controller.getModuleId(EIndex.RUNNING)

    def addBusEventListener(self, listener: IBusDataListener):
        self.bushandler.addBusEventListener(listener)

    def removeBusEventListener(self, listener: IBusDataListener):
        self.bushandler.removeBusEventListener(listener)

    def addBusDeviceListener(self, listener: IBusDeviceListener):
        if not listener in self.device_listeners:
          self.device_listeners.append(listener)

    def removeBusDeviceListener(self, listener: IBusDeviceListener):
        self.device_listeners.remove(listener)

    def is_any_device_found(self) -> bool:
        return self._receivedSomething

    def is_internal_device(self, deviceId:int) -> bool:
        # if deviceId in [110, 503, 1000, 1541, 3422, 4000, 4001, 4002, 4003, 4004, 4005, 4009, 4096, 5068, 8192, 8270, 11581, 12223, 12622, 13976, 14896, 18343, 19075, 20043, 21336, 22909, 24261, 25661, 25874, 28900, 3423, 4006, 4008]:
        #   return True
        return deviceId in {HOMESERVER_DEVICE_ID, 9999, 12222}

    def get_configuration_from_cache(self, device_id: int) -> Configuration:

        configuration = self.configurations.get(device_id)

        if configuration is None:
          LOGGER.debug("reading configuration for cache for {device_id}")
          configuration = Controller.create(device_id, 1).getConfiguration()

        return configuration

    def get_module_id_from_cache(self, device_id: int) -> Configuration:

        module_id = self.module_ids.get(device_id)

        if module_id is None:
          LOGGER.debug("reading module_id for cache for {device_id}")
          module_id = Controller.create(device_id, 1).getModuleId()

        return module_id

    def get_model(self, device_id: int) -> str:

        configuration = self.get_configuration_from_cache(device_id)
        fcke = configuration.getFCKE()
        # special_type = configuration.getStartupDelay()

        firmware_id = self.get_module_id_from_cache(device_id).getFirmwareId()

        model = Templates.get_instance().getModuleName(firmware_id, fcke)

        LOGGER.debug(f"device_id {device_id} fcke {fcke} firmwareId {firmware_id} is model {model}")
        return model

    def busDataReceived(self, busDataMessage):
        """if a device restarts during runtime, we automatically read moduleId"""

        device_id = ObjectId(busDataMessage.getSenderObjectId()).getDeviceId()

        if self.is_internal_device(device_id):
          return

        # ignore own messages
        if not device_id == HOMESERVER_DEVICE_ID:
          self._receivedSomething = True

        if isinstance(busDataMessage.getData(), ModuleId):
            self.module_ids[device_id] = busDataMessage.getData()
            self.known_devices.add(device_id)
            self.collector.add_response(device_id)
            # LOGGER.debug("auto calling getConfiguration")
            # Controller(busDataMessage.getSenderObjectId()).getConfiguration()

        if not device_id in self.known_devices:
          LOGGER.debug(f"got message from unknown device {device_id}. reading module_id");
          Controller.create(device_id, 1).getModuleId(EIndex.RUNNING)

        if isinstance(busDataMessage.getData(), Configuration):
            self.configurations[device_id] = busDataMessage.getData()
            # LOGGER.debug("auto calling getRemoteObjects")
            # Controller(busDataMessage.getSenderObjectId()).getRemoteObjects()

        if isinstance(busDataMessage.getData(), RemoteObjects):
            self.remote_objects[device_id] = busDataMessage.getData()

        """ if a device restarts during runtime, we automatically read moduleId"""
        if isinstance(busDataMessage.getData(), EvStarted):
            LOGGER.debug("auto calling getModuleId")
            Controller(busDataMessage.getSenderObjectId()).getModuleId(EIndex.RUNNING)


# --- Worker-Thread-Klasse ---
class DeviceWorker(threading.Thread):

    def __init__(self, homeserver):
        super().__init__(daemon=True)
        self.queue = queue.Queue()
        self.running = True
        self.homeserver = homeserver

    def run(self):
        timeout = 3  # Sekunden
        LOGGER.debug("Worker gestartet.")
        while self.running:
            try:
                # Warte auf neues Device
                device_id = self.queue.get(timeout=1)
            except queue.Empty:
                continue

            try:
                module_Id = self.homeserver.module_ids[device_id]
                if module_Id is not None:
                  start = time.perf_counter()
                  LOGGER.debug(f"[DeviceWorker {device_id}] Working with module_id {module_Id}")
                  self.homeserver.configurations[device_id] = None
                  Controller.create(device_id, 1).getConfiguration()

                  for _ in range(2):
                      start_time = time.time()
                      while self.homeserver.configurations.get(device_id) is None:
                          if time.time() - start_time > timeout:
                              LOGGER.debug(f"[DeviceWorker {device_id}] Timeout for configuration")
                              break

                          time.sleep(0.1)  # kurze Pause, um CPU nicht zu blockieren

                  configuration = self.homeserver.configurations.get(device_id)
                  if configuration is not None:
                    LOGGER.debug(f"[DeviceWorker {device_id}] got configuration. reading remoteobjects")
                    self.homeserver.remote_objects[device_id] = None
                    Controller.create(device_id, 1).getRemoteObjects()

                    for _ in range(2):
                        start_time = time.time()
                        while self.homeserver.remote_objects.get(device_id) is None:
                          if time.time() - start_time > timeout:
                            LOGGER.debug(f"[DeviceWorker {device_id}] Timeout for remote objects")
                            break

                          time.sleep(0.1)  # kurze Pause, um CPU nicht zu blockieren

                    remote_objects = self.homeserver.remote_objects.get(device_id)
                    if remote_objects is not None:
                      instances = self.getHomeassistantChannels(device_id, remote_objects)
                       
                      end = time.perf_counter()
                      LOGGER.debug(f"[DeviceWorker {device_id}] discovery finished after {end - start:.6f} seconds")
        
                      for actListener in self.homeserver.device_listeners:
                        actListener.newDeviceDetected(device_id, self.homeserver.get_model(device_id), module_Id, configuration, instances)

            except Exception as e:
                logging.error("[DeviceWorker {device_id}] error for %s %s\n%s", e, device_id, traceback.format_exc())
            finally:
                self.queue.task_done()

        LOGGER.debug("[DeviceWorker]  finished.")

    def getHomeassistantChannels(self, device_id: int, remoteObjects: RemoteObjects):

        firmware_id = self.homeserver.get_module_id_from_cache(device_id).getFirmwareId()
        fcke = self.homeserver.get_configuration_from_cache(device_id).getFCKE()
        instances: list[ABusFeature] = self.getDeviceInstances(device_id, remoteObjects)
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

    def getDeviceInstances(self, device_id: int, remoteObjects: RemoteObjects):

        objectList = remoteObjects.getObjectList()
        result = []
        for i in range(0, len(objectList), 2):
            instanceId = objectList[i]
            classId = objectList[i + 1]
            className = ProxyFactory.getBusClassNameForClass(classId)
            objectId = HausBusUtils.getObjectId(device_id, classId, instanceId)

            try:
                class_name = className.rsplit(".", 1)[-1]
                
                full_module_path = className

                # Modul aus Cache
                if full_module_path in _module_cache:
                    module = _module_cache[full_module_path]
                else:
                    module = importlib.import_module(full_module_path)
                _module_cache[full_module_path] = module

                # Klasse aus Cache
                key = (full_module_path, class_name)
                if key in _class_cache:
                    cls = _class_cache[key]
                else:
                    cls = getattr(module, class_name)
                _class_cache[key] = cls

                obj = cls(objectId)
                result.append(obj)
                
            except Exception as err:
                LOGGER.error(err, exc_info=True, stack_info=True)
                
        return result

    def enqueue(self, device_id):
        LOGGER.debug(f"added {device_id} to queue")
        self.queue.put(device_id)

    def stop(self):
        LOGGER.debug("stopping worker")
        self.running = False


# --- Collector, der Geraeteantworten einsammelt ---
class DeviceCollector(threading.Thread):

    def __init__(self, worker, timeout=1.0):
        super().__init__(daemon=True)
        self.worker = worker
        self.timeout = timeout
        self.responses = set()
        self.last_added = 0
        self.lock = threading.Lock()
        self.running = True

    def add_response(self, device_id):
        with self.lock:
            self.responses.add(device_id)
            self.last_added = time.time()
            # Debug
            LOGGER.debug(f"[DeviceCollector] got response from {device_id}")

    def run(self):
        LOGGER.debug("[DeviceCollector] started.")
        while self.running:
            time.sleep(0.1)
            with self.lock:
                # Wenn laenger als timeout keine neue Antwort kam
                if self.responses and (time.time() - self.last_added > self.timeout):
                    devices = list(self.responses)
                    self.responses.clear()
                else:
                    devices = []
            # Ausserhalb des Locks abarbeiten
            for dev in devices:
                LOGGER.debug(f"[DeviceCollector] providing {dev} to worker.")
                self.worker.enqueue(dev)
        LOGGER.debug("[DeviceCollector] finished")

    def stop(self):
        self.running = False
