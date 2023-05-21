from abc import ABC, abstractmethod

class IBusDataListener(ABC):

    @abstractmethod
    def busDataReceived(self,busDataMessage):
        pass