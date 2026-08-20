class JobApplication:
    def __init__(
        self,
        application_id,
        company,
        role,
        location,
        application_date,
        status,
        skills,
        notes=""
    ):
        self.application_id = application_id
        self.company = company
        self.role = role
        self.location = location
        self.application_date = application_date
        self.status = status
        self.skills = skills
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.application_id,
            "company": self.company,
            "role": self.role,
            "location": self.location,
            "application_date": self.application_date,
            "status": self.status,
            "skills": self.skills,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["company"],
            data["role"],
            data["location"],
            data["application_date"],
            data["status"],
            data["skills"],
            data.get("notes", "")
        )