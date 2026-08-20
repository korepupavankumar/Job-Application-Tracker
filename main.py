from manager import JobApplicationManager
from storage import load_applications, save_applications


def display(applications):
    if not applications:
        print("\nNo applications found.")
        return

    print("\n" + "=" * 70)

    for app in applications:
        print(f"ID       : {app.application_id}")
        print(f"Company  : {app.company}")
        print(f"Role     : {app.role}")
        print(f"Location : {app.location}")
        print(f"Date     : {app.application_date}")
        print(f"Status   : {app.status}")
        print(f"Skills   : {', '.join(app.skills)}")
        print(f"Notes    : {app.notes}")
        print("-" * 70)


def main():
    applications = load_applications()
    manager = JobApplicationManager(applications)

    while True:

        print("\n===== JOB APPLICATION TRACKER =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Search Application")
        print("4. Filter by Status")
        print("5. Update Status")
        print("6. Delete Application")
        print("7. Statistics")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                # Validate Application ID immediately
                while True:
                    app_id = input(
                        "Application ID (example: AP001): "
                    ).strip().upper()

                    if (
                        len(app_id) == 5
                        and app_id.startswith("AP")
                        and app_id[2:].isdigit()
                    ):
                        break

                    print("Invalid ID. Please use format AP001.")

                company = input("Company: ")
                role = input("Role: ")
                location = input("Location: ")
                date = input(
                    "Application Date (YYYY-MM-DD): "
                )
                status = input("Status: ")

                skills = input(
                    "Skills (comma separated): "
                ).split(",")

                skills = [
                    skill.strip()
                    for skill in skills
                    if skill.strip()
                ]

                notes = input("Notes: ")

                manager.add(
                    app_id,
                    company,
                    role,
                    location,
                    date,
                    status,
                    skills,
                    notes
                )

                save_applications(manager.applications)

                print("Application added successfully.")

            elif choice == "2":
                display(manager.view_all())

            elif choice == "3":

                keyword = input(
                    "Search company or role: "
                )

                results = manager.search(keyword)

                display(results)

            elif choice == "4":

                status = input("Enter status: ")

                results = manager.filter_by_status(status)

                display(results)

            elif choice == "5":

                app_id = input("Application ID: ")
                status = input("New status: ")

                manager.update_status(app_id, status)

                save_applications(manager.applications)

                print("Status updated successfully.")

            elif choice == "6":

                app_id = input("Application ID: ")

                manager.delete(app_id)

                save_applications(manager.applications)

                print("Application deleted successfully.")

            elif choice == "7":

                stats = manager.statistics()

                print("\n===== APPLICATION STATISTICS =====")

                for status, count in stats.items():
                    print(f"{status}: {count}")

            elif choice == "8":

                save_applications(manager.applications)

                print(
                    "Thank you for using "
                    "Job Application Tracker."
                )
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
