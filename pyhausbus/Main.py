from pyhausbus.HausBusCommand import HausBusCommand
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.HomeServer import HomeServer
from pyhausbus.IBusDataListener import IBusDataListener
from pyhausbus.ObjectId import ObjectId
from pyhausbus.de.hausbus.homeassistant.proxy.Controller import Controller
from pyhausbus.de.hausbus.homeassistant.proxy.Taster import Taster
from pyhausbus.de.hausbus.homeassistant.proxy.Dimmer import Dimmer
from pyhausbus.de.hausbus.homeassistant.proxy.Schalter import Schalter
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import RemoteObjects
from pyhausbus.de.hausbus.homeassistant.proxy.LogicalButton import LogicalButton
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params import EIndex
from pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Configuration import Configuration


class Main(IBusDataListener):

  def __init__(self):

    ''' 
    Instantiate Homeserver, add as Lister and search Devices
    Afterwards all devices respond with their moduleId. See method busDataReceived
    '''
    self.server = HomeServer()
    self.server.addBusEventListener(self)
    self.server.searchDevices()

    ''' Example how to directly create a feature with given ObjectId'''
    taster = Taster(1313542180)
    taster.getConfiguration();

    ''' Example how to directly create a feature with given class and intance id'''
    deckenLicht = Dimmer.create(22784, 5)
    deckenLicht.setBrightness(0, 0)

  def busDataReceived(self, busDataMessage):
    print("got: " + str(busDataMessage.getData()) + " from " + str(ObjectId(busDataMessage.getSenderObjectId())) + " to " + str(ObjectId(busDataMessage.getReceiverObjectId())))

    if (isinstance(busDataMessage.getData(), ModuleId)):
      Controller(busDataMessage.getSenderObjectId()).getRemoteObjects()

    if (isinstance(busDataMessage.getData(), RemoteObjects)):
      instances = self.server.getDeviceInstances(busDataMessage.getSenderObjectId(), busDataMessage.getData())
      for actInstance in instances:
        print (actInstance)


Main()
