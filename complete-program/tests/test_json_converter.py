import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from json_converter import FileWay, JsonConversion, JsonConverter


class JsonConverterTests(unittest.TestCase):
    def test_writes_json_data_to_file(self) -> None:
        data = {"message": "Привет", "items": [1, True, None]}

        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "output.json"
            converter = JsonConverter(data, FileWay(output_path))

            result_path = converter.convert()

            self.assertEqual(result_path, output_path)
            self.assertEqual(json.loads(output_path.read_text(encoding="utf-8")), data)

    def test_rejects_non_finite_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            converter = JsonConverter(float("nan"), FileWay(Path(directory) / "output.json"))

            with self.assertRaises(ValueError):
                converter.convert()

    def test_conversion_strategy_is_used(self) -> None:
        class RecordingConversion(JsonConversion):
            def __init__(self) -> None:
                self.received_data: Any = None

            def convert(self, data: Any) -> Path:
                self.received_data = data
                return Path("recorded.json")

        data = {"value": 42}
        strategy = RecordingConversion()

        output_path = JsonConverter(data, strategy).convert()

        self.assertEqual(strategy.received_data, data)
        self.assertEqual(output_path, Path("recorded.json"))


if __name__ == "__main__":
    unittest.main()
