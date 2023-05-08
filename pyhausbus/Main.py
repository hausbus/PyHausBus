from HomeServer import HomeServer
from de.hausbus.homeassistant.proxy.Controller import Controller
from HausBusCommand import HausBusCommand
from IBusDataListener import IBusDataListener
from ObjectId import ObjectId
from de.hausbus.homeassistant.proxy.Schalter import Schalter
from de.hausbus.homeassistant.proxy.Dimmer import Dimmer
import HausBusUtils
from de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from de.hausbus.homeassistant.proxy.controller.data.RemoteObjects import RemoteObjects

class Main(IBusDataListener):
  
  def __init__(self):
    self.server = HomeServer()
    self.server.addBusEventListener(self)
    self.server.searchDevices()
    
    deckenLicht=Dimmer(HausBusUtils.getObjectId(22784, Dimmer.CLASS_ID, 5))
    deckenLicht.setBrightness(0, 0)
    
  def busDataReceived(self,busDataMessage):
    print("got: "+str(busDataMessage.getData())+" from "+str(ObjectId(busDataMessage.getSenderObjectId()))+" to "+str(ObjectId(busDataMessage.getReceiverObjectId())))

    if (isinstance(busDataMessage.getData(), ModuleId)):
      Controller(busDataMessage.getSenderObjectId()).getRemoteObjects()

    if (isinstance(busDataMessage.getData(), RemoteObjects)):
      instances = self.server.getDeviceInstances(busDataMessage.getSenderObjectId(), busDataMessage.getData())
      for actInstance in instances:
        print (actInstance)

Main()