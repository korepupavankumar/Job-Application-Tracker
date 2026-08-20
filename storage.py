import json
from pathlib import Path

from models import JobApplication


FILE = Path(__file__).parent / "data" / "applications.json"


def load_applications():
    if not FILE.exists():
        return []

    try:
        with open(FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [
            JobApplication.from_dict(item)
            for item in data
        ]

    except (json.JSONDecodeError, KeyError):
        return []


def save_applications(applications):
    FILE.parent.mkdir(exist_ok=True)

    data = [
        application.to_dict()
        for application in applications
    ]

    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)