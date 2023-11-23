from pyhausbus.HomeServer import HomeServer
from pyhausbus.ResultWorker import ResultWorker
from pyhausbus.IBusDataListener import IBusDataListener
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
import pyhausbus.HausBusUtils
from pyhausbus.ObjectId import ObjectId
import time

class Main(IBusDataListener):

  def __init__(self):

    '''
    Instantiate Homeserver, add as Lister and search Devices
    Afterwards all devices respond with their moduleId. See method busDataReceived
    '''
    self.server = HomeServer()
    self.server.addBusEventListener(self)
    '''self.server.searchDevices()'''

    ''' Example how to directly create a feature with given class and instance id'''
    Dimmer.create(22784, 5).setBrightness(100, 0)

    ''' Example how to directly create a feature with given ObjectId and wait for the result '''
    taster = Taster(1313542180)
    ''' Then we call the method'''
    taster.getConfiguration()
    ''' And then wait for the Result with a timeout of 2 seconds'''
    configuration = ResultWorker().waitForResult(2)
    print("configuration = "+str(configuration))

    self.doTests()




  def busDataReceived(self, busDataMessage):
    print("got: " + str(busDataMessage.getData()) + " from " + str(ObjectId(busDataMessage.getSenderObjectId())) + " to " + str(ObjectId(busDataMessage.getReceiverObjectId())))

    if (isinstance(busDataMessage.getData(), RemoteObjects)):
      instances = self.server.getDeviceInstances(busDataMessage.getSenderObjectId(), busDataMessage.getData())
      for actInstance in instances:
        print (actInstance)


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
