from models import JobApplication
from validators import (
    validate_text,
    validate_date,
    validate_status
)


class JobApplicationManager:

    def __init__(self, applications):
        self.applications = applications

    def add(self, application_id, company, role,
            location, date, status, skills, notes):

        for app in self.applications:
            if app.application_id == application_id:
                raise ValueError("Application ID already exists.")

        application = JobApplication(
            application_id,
            validate_text(company, "Company"),
            validate_text(role, "Role"),
            validate_text(location, "Location"),
            validate_date(date),
            validate_status(status),
            skills,
            notes
        )

        self.applications.append(application)

    def view_all(self):
        return self.applications

    def search(self, keyword):
        keyword = keyword.lower()

        return [
            app for app in self.applications
            if keyword in app.company.lower()
            or keyword in app.role.lower()
        ]

    def filter_by_status(self, status):
        status = validate_status(status)

        return [
            app for app in self.applications
            if app.status == status
        ]

    def update_status(self, application_id, status):
        for app in self.applications:
            if app.application_id == application_id:
                app.status = validate_status(status)
                return

        raise ValueError("Application not found.")

    def delete(self, application_id):
        for app in self.applications:
            if app.application_id == application_id:
                self.applications.remove(app)
                return

        raise ValueError("Application not found.")

    def statistics(self):
        result = {}

        for app in self.applications:
            result[app.status] = result.get(app.status, 0) + 1

        return result