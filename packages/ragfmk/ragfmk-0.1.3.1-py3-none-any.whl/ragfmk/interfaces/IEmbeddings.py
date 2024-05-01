__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

from abc import ABC, abstractmethod

class IEmbeddings(ABC):
    
    @property
    @abstractmethod
    def content(self):
        return None
    @content.setter
    def content(self, q):
        pass
    
    @property
    @abstractmethod
    def jsonContent(self):
        return None
    
    @property
    @abstractmethod
    def size(self):
        return None
    
    @abstractmethod
    def encode(self, cks):
        pass
    
    @abstractmethod
    def create(self, cks):
        pass
    
    @abstractmethod
    def save(self, filename):
        pass
    
    @abstractmethod
    def load(self, filename = "", content = ""):
        pass