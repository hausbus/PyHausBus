from pyhausbus.HomeServer import HomeServer
from pyhausbus.ResultWorker import ResultWorker
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.IBusDeviceListener import IBusDeviceListener
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
from pyhausbus.de.hausbus.homeassistant.proxy.Taster import Taster
from pyhausbus.de.hausbus.homeassistant.proxy.Led import Led
from pyhausbus.de.hausbus.homeassistant.proxy.Dimmer import Dimmer
from pyhausbus.de.hausbus.homeassistant.proxy.Schalter import Schalter
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import RemoteObjects
from pyhausbus.de.hausbus.homeassistant.proxy.LogicalButton import LogicalButton
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.params.EDirection import EDirection
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvOn import EvOn
from pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvOff import EvOff
from pyhausbus.de.hausbus.homeassistant.proxy.Feuchtesensor import Feuchtesensor
from pyhausbus.ABusFeature import ABusFeature
import pyhausbus.HausBusUtils
import logging
from pyhausbus.ObjectId import ObjectId
import time
LOGGER = logging.getLogger("pyhausbus")

class Main(IBusDataListener, IBusDeviceListener):

  def __init__(self):
    
    logging.basicConfig(
      level=logging.DEBUG,  # alle Meldungen ab DEBUG
      format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
      datefmt="%Y-%m-%d %H:%M:%S:%S",  # Format fuer den Timestamp
      filename="mein_log.log",                    # Name der Log-Datei
      filemode="w"                                # 'a' = anhaengen, 'w' = ueberschreiben
    )
    
    '''
    Instantiate Homeserver, add as Lister and search Devices
    Afterwards all devices respond with their moduleId. See method busDataReceived
    '''
    self.server = HomeServer()
    self.server.addBusDeviceListener(self)
    #self.server.addBusEventListener(self)
    self.server.searchDevices()

    ''' Example how to directly create a feature with given class and instance id'''
    #Dimmer.create(22784, 5).setBrightness(100, 0)

    ''' Example how to directly create a feature with given ObjectId and wait for the result '''
    #taster = Taster(1313542180)
    ''' Then we call the method'''
    #taster.getConfiguration()
    ''' And then wait for the Result with a timeout of 2 seconds'''
    #configuration = ResultWorker().waitForResult(2)
    #print("configuration = "+str(configuration))

    #self.doTests()


  def busDataReceived(self, busDataMessage):
      LOGGER.debug("got: " + str(busDataMessage.getData()) + " from " + str(ObjectId(busDataMessage.getSenderObjectId())) + " to " + str(ObjectId(busDataMessage.getReceiverObjectId())))

  def newDeviceDetected(self,device_id:int, model_type: str, module_id: ModuleId, configuration: Configuration, channels: list[ABusFeature]):
      LOGGER.info(f"newDeviceDetected {device_id} model_type {model_type} module_id {module_id} configuration {configuration}")
      for actFeature in channels:
        LOGGER.info(f"channel {actFeature}")

  def doTests(self):

    controller = Controller.create(3359, 1)
    controller.getConfiguration()
    print("Controller.configuration = "+str(ResultWorker().waitForResult(2)))
    controller.getModuleId(EIndex.EIndex.RUNNING)
    print("Controller.moduleId = "+str(ResultWorker().waitForResult(2)))
    controller.ping()
    print("Controller.pong = "+str(ResultWorker().waitForResult(2)))

    dimmer = Dimmer.create(22784, 5)
    dimmer.getConfiguration()
    print("Dimmer.configuration = "+str(ResultWorker().waitForResult(2)))
    dimmer.getStatus()
    print("Dimmer.status = "+str(ResultWorker().waitForResult(2)))
    dimmer.start(EDirection.TO_LIGHT)
    print("Dimmer.evOn = "+str(ResultWorker().waitForEvent(EvOn, dimmer.getObjectId(), 5)))
    dimmer.start(EDirection.TO_DARK)
    print("Dimmer.evOff = "+str(ResultWorker().waitForEvent(EvOff, dimmer.getObjectId(), 5)))

    feuchtesensor = Feuchtesensor.create(25661 , 88)
    feuchtesensor.getConfiguration()
    print("Feuchtesensor.configuration = "+str(ResultWorker().waitForResult(2)))
    feuchtesensor.getStatus()
    print("Feuchtesensor.status = "+str(ResultWorker().waitForResult(2)))

    led = Led.create(20043,54)
    led.getConfiguration()
    print("Led.configuration = "+str(ResultWorker().waitForResult(2)))
    led.getStatus()
    print("Led.status = "+str(ResultWorker().waitForResult(2)))
    led.on(50, 5, 0)
    led.getStatus()
    print("Led.status = "+str(ResultWorker().waitForResult(2)))
    time.sleep(2)
    led.getStatus()
    print("Led.status = "+str(ResultWorker().waitForResult(2)))
    time.sleep(3)
    led.getStatus()
    print("Led.status = "+str(ResultWorker().waitForResult(2)))

Main()
