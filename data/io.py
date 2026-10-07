import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent


def load_json(filename):
    file_path = PROJECT_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)