import json
from jsonschema import validate, ValidationError
from pathlib import Path


APP_NAME = "collection_manager"

COLLECTION_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "description": {
                "type": "string",
            },
            "quantity": {
                "type": "integer",
                "minimum": 0,
            },
        },
        "required": ["name", "description", "quantity"],
    },
}


def get_data_file_path() -> Path:
    data_dir = Path.home() / ".local" / "share" / APP_NAME
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "collections.json"
    return file_path


def save_data(data: list):
    try:
        validate(instance=data, schema=COLLECTION_SCHEMA)
    except ValidationError as e:
        print(f"Data validation error: {e.message}")
        return

    file_path = get_data_file_path()

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    file_path = get_data_file_path()
    data = None

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Data not loaded correctly")
        return []

    try:
        validate(instance=data, schema=COLLECTION_SCHEMA)
    except ValidationError as e:
        print(f"Data validation error: {e.message}")
        return []

    return data
