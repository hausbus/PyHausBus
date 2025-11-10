from abc import ABC, abstractmethod
from pyhausbus.ABusFeature import ABusFeature
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId import ModuleId
from pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Configuration import Configuration

class IBusDeviceListener(ABC):

    @abstractmethod
    def newDeviceDetected(self,device_id:int, model_type: str, module_id: ModuleId, configuration: Configuration, channels: list[ABusFeature]):
        pass