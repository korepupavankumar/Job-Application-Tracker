from datetime import datetime


VALID_STATUSES = [
    "Applied",
    "Shortlisted",
    "Interview",
    "Selected",
    "Rejected"
]


def validate_text(value, field):
    value = value.strip()

    if not value:
        raise ValueError(f"{field} cannot be empty.")

    return value


def validate_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        raise ValueError("Date must be YYYY-MM-DD.")


def validate_status(status):
    status = status.strip().title()

    if status not in VALID_STATUSES:
        raise ValueError(
            "Status must be: "
            + ", ".join(VALID_STATUSES)
        )

    return status