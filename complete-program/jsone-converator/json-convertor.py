import json
from typing import List, Any, Set
import pathlib
from abc import ABC, abstractmethod
class Convert_to_json(ABC):
    @abstractmethod
    def convert_to_json(self) -> str:
        pass
class FileWay(Convert_to_json):
    def __init__(self, file_path: pathlib.Path):
        self.__file_path = file_path

    def convert_to_json(self) -> str:
        return json.dumps(self.__file_path.read_text())

class Convertor:
    def __init__(self, data: List[Any]):
        self.__data = data
    @property
    def data(self) -> List[Any]:
        return self.__data
    @data.setter
    def data(self, value: List[Any]):
        if self.__data is not None:
            raise ValueError("Data has already been set and cannot be modified.")
        elif not isinstance(value, list):
            raise TypeError("Data must be a list.")
        elif not all(isinstance(item, (int, float, str, dict, list)) for item in value):
            raise ValueError("All items in the data list must be of type int, float, str, dict, or list.")
        elif len(value) == 0:
            raise ValueError("Data list cannot be empty.")
        elif len(value) > 100:
            raise ValueError("Data list cannot contain more than 100 items.")
        elif any(isinstance(item, dict) and len(item) > 10 for item in value):
            raise ValueError("Dictionaries in the data list cannot contain more than 10 key-value pairs.")
        else:
            print("Data is valid and has been set.")
        self.__data = value
    @getconvert_to_json.setter
    def getconvert_to_json(self, value: Convert_to_json):
        if not isinstance(value, Convert_to_json):
            raise TypeError("Value must be an instance of Convert_to_json.")
        self.__convert_to_json = value
        def convert_to_json(value) -> Set[str]:
                def elements(data):
                    if isinstance(data, dict):
                        for key, value in data.items():
                            yield key
                            yield from elements(value)
                    elif isinstance(data, list):
                        for item in data:
                            yield from elements(item)
                    else:
                        yield data
                with open("output.json", "w") as f:
                    json.dump(self.__data, f, indent=4)
                return { "output.json" }
    
    