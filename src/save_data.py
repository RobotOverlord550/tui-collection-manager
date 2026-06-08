import json
from jsonschema import validate, ValidationError
from pathlib import Path


APP_NAME = "collection_manager"

COLLECTION_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "quantity": {"type": "integer", "minimum": 0},
    },
    "required": ["name", "description", "quantity"],
}


def save_data(data: dict):
    try:
        validate(instance=data, schema=COLLECTION_SCHEMA)
    except ValidationError as e:
        print(f"Data validation error: {e.message}")

    data_dir = Path.home() / ".local" / "share" / APP_NAME
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "collections.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
