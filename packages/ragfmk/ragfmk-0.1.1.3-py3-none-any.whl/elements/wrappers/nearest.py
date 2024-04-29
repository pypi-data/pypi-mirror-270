__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

import utils.CONST as C
import json
from numpyencoder import NumpyEncoder

""" Manages the Chunks file structure (JSON)
    Content = {"chunks": [..., ...] }
"""

class nearest:
    def __init__(self):
        self.__items = [] # simple Array which contains all the items
    
    @property
    def list(self): 
        return self.__items 
    @list.setter
    def list(self, q):
        self.__items = q

    @property
    def jsonContent(self) -> str: 
        return json.dumps(self.__createEnveloppe(), cls=NumpyEncoder)

    @property
    def size(self) -> list: 
        return len(self.list)
    
    def __createEnveloppe(self) -> str:
        jsonEnv = {}
        jsonEnv[C.JST_NEAREST] = self.list
        return jsonEnv
    
    def add(self, item):
        self.__items.append(item)

    def save(self, filename) -> bool:
        """ Save the chunks in a file.
        Args:
            filename (_type_): JSON chunks file
        Returns:
            bool: True if ok
        """
        try:
            with open(filename, "w", encoding=C.ENCODING) as f:
                f.write(self.jsonContent)
            return True
        except Exception as e:
            return False

    def load(self, filename = "", content = "") -> bool:
        """ Load and build a chunk file (can be loaded from a json file or a json content). 
            Format required : Content = {"chunks": [..., ...] }
        Args:
            filename (str, optional): JSON chunks file. Defaults to "".
            content (str, optional): JSON chunks content. Defaults to "".
        Returns:
            bool: True if ok
        """
        try:
            jsonEnv = ""
            if (len(filename) >0):
                with open(filename, "r", encoding=C.ENCODING) as f:
                    jsonEnv = json.load(f)
            elif (len(content) >0):
                jsonEnv = content
            else:
                return False
            self.list = jsonEnv[C.JST_NEAREST]
            return True
        except Exception as e:
            return False