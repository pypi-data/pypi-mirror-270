__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

from abc import ABC, abstractmethod

class INearest(ABC):

    @property
    @abstractmethod
    def items(self): 
        return None 
    @items.setter
    def items(self, q):
        pass
    
    @property
    @abstractmethod
    def distances(self): 
        return None 
    @distances.setter
    def distances(self, q):
        pass
    
    @property
    @abstractmethod
    def jsonContent(self): 
        return None
    
    @property
    @abstractmethod
    def size(self) -> items: 
        return None
    
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def save(self, filename):
        pass
    
    @abstractmethod
    def load(self, filename, content):
        pass