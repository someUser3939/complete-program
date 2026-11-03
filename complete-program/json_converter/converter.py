import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class JsonConversion(ABC):
    @abstractmethod
    def convert(self, data: Any) -> Path:
        """Convert data to JSON and persist it."""


class FileWay(JsonConversion):
    def __init__(self, file_path: Path) -> None:
        self._file_path = file_path

    def convert(self, data: Any) -> Path:
        json_data = json.dumps(data, ensure_ascii=False, indent=4, allow_nan=False)
        self._file_path.write_text(json_data + "\n", encoding="utf-8")
        return self._file_path


class JsonConverter:
    def __init__(self, data: Any, conversion: JsonConversion) -> None:
        self._data = data
        self._conversion = conversion

    @property
    def data(self) -> Any:
        return self._data

    def convert(self) -> Path:
        return self._conversion.convert(self._data)
