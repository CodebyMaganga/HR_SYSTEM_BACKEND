from app import app
from models import db, Admin, Employee, Project, Dependant, Document, Reference, JobApplicant, Interview, Department, BankDetail, Leave
from datetime import datetime, timedelta

with app.app_context():
    db.create_all()
    departments = [
        Department(department_name="Human Resources"),
        Department(department_name="Engineering"),
        Department(department_name="Marketing"),
        Department(department_name="Sales"),
        Department(department_name="Finance")
    ]
    db.session.bulk_save_objects(departments)
    db.session.commit()

    # Employees
    employees = [
        Employee(first_name="John", last_name="Doe", national_ID="123456", gender="Male", DOB=datetime.strptime("1990-01-01", "%Y-%m-%d"), email="john@example.com", phone="555-0001", address="123 Main St", role="Engineer", active_status=True, profile_picture="path/to/picture1.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country1", emergency_contact="555-1001"),
        Employee(first_name="Jane", last_name="Smith", national_ID="123457", gender="Female", DOB=datetime.strptime("1991-02-02", "%Y-%m-%d"), email="jane@example.com", phone="555-0002", address="456 Side St", role="HR Manager", active_status=True, profile_picture="path/to/picture2.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country2", emergency_contact="555-1002"),
        # ... add 3 more employees
    ]
    db.session.bulk_save_objects(employees)

    # Dependants
    dependants = [
        Dependant(first_name="Alice", last_name="Doe", gender="Female", age=4, relationship="Daughter", employee_id=1),
        Dependant(first_name="Bob", last_name="Doe", gender="Male", age=2, relationship="Son", employee_id=1),
        # ... add 3 more dependants
    ]
    db.session.bulk_save_objects(dependants)

    # References
    references = [
        Reference(reference_name="Charlie Smith", reference_phone="555-2001", employee_id=1),
        Reference(reference_name="Diana Jones", reference_phone="555-2002", employee_id=2),
        # ... add 3 more references
    ]
    db.session.bulk_save_objects(references)

    # BankDetails
    bank_details = [
        BankDetail(employee_salary="70000", employee_account="ACC123456", employee_bank="Bank1", branch_code="BR001", employee_id=1),
        BankDetail(employee_salary="80000", employee_account="ACC123457", employee_bank="Bank2", branch_code="BR002", employee_id=2),
        # ... add 3 more bank details
    ]
    db.session.bulk_save_objects(bank_details)

    # # Managers
    # managers = [
    #     Manager(employee_id=2),
    #     Manager(employee_id=3),
    #     # ... add 3 more managers
    # ]
    # db.session.bulk_save_objects(managers)

    # Projects
    projects = [
        Project(title="Project 1", project_status="Active"),
        Project(title="Project 2", project_status="Completed"),
        # ... add 3 more projects
    ]
    db.session.bulk_save_objects(projects)

    # Leaves
    leaves = [
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=10), leave_type="Annual", leave_letter="path/to/letter1.jpg"),
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=5), leave_type="Sick", leave_letter="path/to/letter2.jpg"),
        # ... add 3 more leaves
    ]
    db.session.bulk_save_objects(leaves)

    # Job Applicants
    job_applicants = [
        JobApplicant(first_name="Eva", last_name="Green", photo="path/to/photo1.jpg", address="789 Down St", experience="5 years", role_applied="Marketing Manager", status="Applied"),
        JobApplicant(first_name="Frank", last_name="Wright", photo="path/to/photo2.jpg", address="321 Up St", experience="3 years", role_applied="Sales Representative", status="Interviewed"),
        # ... add 3 more job applicants
    ]
    db.session.bulk_save_objects(job_applicants)

    # Interviews
    interviews = [
        Interview(time=datetime.now() + timedelta(days=1), applicant_id=1),
        Interview(time=datetime.now() + timedelta(days=3), applicant_id=2),
        # ... add 3 more interviews
    ]
    db.session.bulk_save_objects(interviews)

    # Documents
    documents = [
        Document(document_type="Contract", employee_id=1),
        Document(document_type="Resume", employee_id=2),
        # ... add 3 more documents
    ]
    db.session.bulk_save_objects(documents)

    db.session.commit()



