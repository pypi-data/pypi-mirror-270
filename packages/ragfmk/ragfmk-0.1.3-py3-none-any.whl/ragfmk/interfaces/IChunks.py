__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

from abc import ABC, abstractmethod

class IChunks(ABC):
    @property
    @abstractmethod
    def items(self): 
        return [] 
    @items.setter
    def items(self, q):
        pass
    
    @property
    @abstractmethod
    def jsonContent(self): 
        return None
    @jsonContent.setter
    def jsonContent(self, content):
        pass
    
    @property
    @abstractmethod
    def size(self): 
        return None
    
    @abstractmethod
    def add(self, chunk):
        pass
    
    @abstractmethod
    def save(self, filename):
        pass
    
    @abstractmethod
    def load(self, filename, content):
        pass
