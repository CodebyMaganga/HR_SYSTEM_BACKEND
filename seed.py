from app import app
from models import db, Admin, Employee, Project, Dependant, Document, Reference, JobApplicant, Interview, Department, BankDetail, Leave, Project_employee, Department_employee, OnLeave_employee
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

    # Employees
    employees = [
        Employee(first_name="John", last_name="Doe", national_ID="123456", gender="Male", DOB=datetime.strptime("1990-01-01", "%Y-%m-%d"), email="john@example.com", phone="555-0001", address="123 Main St", role="Engineer", active_status=True, profile_picture="path/to/picture1.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country1", emergency_contact="555-1001"),
        Employee(first_name="Jane", last_name="Smith", national_ID="123457", gender="Female", DOB=datetime.strptime("1991-02-02", "%Y-%m-%d"), email="jane@example.com", phone="555-0002", address="456 Side St", role="HR Manager", active_status=True, profile_picture="path/to/picture2.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country2", emergency_contact="555-1002"),
        Employee(first_name="Alice", last_name="Johnson", national_ID="345678", gender="Female", DOB=datetime.strptime("1988-03-03", "%Y-%m-%d"), email="alice.johnson@example.com", phone="555-0003", address="789 Third St", role="Project Manager", active_status=True, profile_picture="path/to/alice.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country3", emergency_contact="555-3003"),
        Employee(first_name="Bob", last_name="Brown", national_ID="456789", gender="Male", DOB=datetime.strptime("1992-04-04", "%Y-%m-%d"), email="bob.brown@example.com", phone="555-0004", address="101 Fourth St", role="Developer", active_status=True, profile_picture="path/to/bob.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country4", emergency_contact="555-4004"),
        Employee(first_name="Carol", last_name="Davis", national_ID="567890", gender="Female", DOB=datetime.strptime("1991-05-05", "%Y-%m-%d"), email="carol.davis@example.com", phone="555-0005", address="202 Fifth St", role="Designer", active_status=True, profile_picture="path/to/carol.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country5", emergency_contact="555-5005"),
        Employee(first_name="David", last_name="Wilson", national_ID="678901", gender="Male", DOB=datetime.strptime("1987-06-06", "%Y-%m-%d"), email="david.wilson@example.com", phone="555-0006", address="303 Sixth St", role="HR", active_status=True, profile_picture="path/to/david.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country6", emergency_contact="555-6006"),
        Employee(first_name="Eva", last_name="Martin", national_ID="789012", gender="Female", DOB=datetime.strptime("1993-07-07", "%Y-%m-%d"), email="eva.martin@example.com", phone="555-0007", address="404 Seventh St", role="Accountant", active_status=True, profile_picture="path/to/eva.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country7", emergency_contact="555-7007"),
        Employee(first_name="Frank", last_name="Garcia", national_ID="890123", gender="Male", DOB=datetime.strptime("1986-08-08", "%Y-%m-%d"), email="frank.garcia@example.com", phone="555-0008", address="505 Eighth St", role="Technician", active_status=True, profile_picture="path/to/frank.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country8", emergency_contact="555-8008"),
        Employee(first_name="Grace", last_name="Lee", national_ID="901234", gender="Female", DOB=datetime.strptime("1989-09-09", "%Y-%m-%d"), email="grace.lee@example.com", phone="555-0009", address="606 Ninth St", role="Sales", active_status=True, profile_picture="path/to/grace.jpg", date_joined=datetime.now(), marital_status="Married", nationality="Country9", emergency_contact="555-9009"),
        Employee(first_name="Henry", last_name="Taylor", national_ID="012345", gender="Male", DOB=datetime.strptime("1994-10-10", "%Y-%m-%d"), email="henry.taylor@example.com", phone="555-0010", address="707 Tenth St", role="Marketing", active_status=True, profile_picture="path/to/henry.jpg", date_joined=datetime.now(), marital_status="Single", nationality="Country10", emergency_contact="555-1010")
    ]
    db.session.bulk_save_objects(employees)

    # Dependants
    dependants = [
        Dependant(first_name="Alice", last_name="Doe", gender="Female", age=4, relationship="Daughter", employee_id=1),
        Dependant(first_name="Bob", last_name="Doe", gender="Male", age=2, relationship="Son", employee_id=1),
        Dependant(first_name="Alice", last_name="Doe", gender="Female", age=4, relationship="Daughter", employee_id=1),
        Dependant(first_name="Bob", last_name="Doe", gender="Male", age=2, relationship="Son", employee_id=1),
        Dependant(first_name="Charlie", last_name="Smith", gender="Male", age=5, relationship="Son", employee_id=2),
        Dependant(first_name="Diana", last_name="Smith", gender="Female", age=3, relationship="Daughter", employee_id=2),
        Dependant(first_name="Ethan", last_name="Johnson", gender="Male", age=6, relationship="Son", employee_id=3),
        Dependant(first_name="Fiona", last_name="Johnson", gender="Female", age=4, relationship="Daughter", employee_id=3),
        Dependant(first_name="George", last_name="Brown", gender="Male", age=7, relationship="Son", employee_id=4),
        Dependant(first_name="Hannah", last_name="Brown", gender="Female", age=5, relationship="Daughter", employee_id=4),
        Dependant(first_name="Ian", last_name="Davis", gender="Male", age=8, relationship="Son", employee_id=5),
        Dependant(first_name="Jill", last_name="Davis", gender="Female", age=6, relationship="Daughter", employee_id=5)
    ]
    db.session.bulk_save_objects(dependants)

    # References
    references = [
        Reference(reference_name="Charlie Smith", reference_phone="555-2001", employee_id=1),
        Reference(reference_name="Diana Jones", reference_phone="555-2002", employee_id=2),
        Reference(reference_name="Charlie Smith", reference_phone="555-2001", employee_id=1),
        Reference(reference_name="Diana Jones", reference_phone="555-2002", employee_id=2),
        Reference(reference_name="Ethan Taylor", reference_phone="555-2003", employee_id=3),
        Reference(reference_name="Fiona White", reference_phone="555-2004", employee_id=4),
        Reference(reference_name="George Brown", reference_phone="555-2005", employee_id=5),
        Reference(reference_name="Hannah Green", reference_phone="555-2006", employee_id=6),
        Reference(reference_name="Ian Black", reference_phone="555-2007", employee_id=7),
        Reference(reference_name="Jill King", reference_phone="555-2008", employee_id=8),
        Reference(reference_name="Kevin Lee", reference_phone="555-2009", employee_id=9),
        Reference(reference_name="Laura Hall", reference_phone="555-2010", employee_id=10)
    ]
    db.session.bulk_save_objects(references)

    # BankDetails
    bank_details = [
        BankDetail(employee_salary="70000", employee_account="ACC123456", employee_bank="Bank1", branch_code="BR001", employee_id=1),
        BankDetail(employee_salary="80000", employee_account="ACC123457", employee_bank="Bank2", branch_code="BR002", employee_id=2),
        BankDetail(employee_salary="75000", employee_account="ACC123458", employee_bank="Bank3", branch_code="BR003", employee_id=3),
        BankDetail(employee_salary="65000", employee_account="ACC123459", employee_bank="Bank4", branch_code="BR004", employee_id=4),
        BankDetail(employee_salary="68000", employee_account="ACC123460", employee_bank="Bank5", branch_code="BR005", employee_id=5),
        BankDetail(employee_salary="72000", employee_account="ACC123461", employee_bank="Bank6", branch_code="BR006", employee_id=6),
        BankDetail(employee_salary="77000", employee_account="ACC123462", employee_bank="Bank7", branch_code="BR007", employee_id=7),
        BankDetail(employee_salary="69000", employee_account="ACC123463", employee_bank="Bank8", branch_code="BR008", employee_id=8),
        BankDetail(employee_salary="81000", employee_account="ACC123464", employee_bank="Bank9", branch_code="BR009", employee_id=9),
        BankDetail(employee_salary="73000", employee_account="ACC123465", employee_bank="Bank10", branch_code="BR010", employee_id=10)
    ]
    db.session.bulk_save_objects(bank_details)


    # Projects
    projects = [
        Project(title="Project 1", project_status="Active"),
        Project(title="Project 2", project_status="Completed"),
        Project(title="Project 1", project_status="Active"),
        Project(title="Project 2", project_status="Completed"),
        Project(title="Project 3", project_status="In Progress"),
        Project(title="Project 4", project_status="Active"),
        Project(title="Project 5", project_status="Planning"),
        Project(title="Project 6", project_status="Completed"),
        Project(title="Project 7", project_status="In Progress"),
        Project(title="Project 8", project_status="Active"),
        Project(title="Project 9", project_status="Planning"),
        Project(title="Project 10", project_status="Completed")
    ]
    db.session.bulk_save_objects(projects)

    # Leaves
    leaves = [
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=10), leave_type="Annual", leave_letter="path/to/letter1.jpg"),
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=5), leave_type="Sick", leave_letter="path/to/letter2.jpg"),
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=10), leave_type="Annual", leave_letter="path/to/letter1.jpg",),
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=5), leave_type="Sick", leave_letter="path/to/letter2.jpg",),
        Leave(leave_from=datetime.now(), leave_to=datetime.now() + timedelta(days=7), leave_type="Annual", leave_letter="path/to/letter6.jpg")
    ]
    db.session.bulk_save_objects(leaves)

    # Job Applicants
    job_applicants = [
        JobApplicant(first_name="Eva", last_name="Green", photo="path/to/photo1.jpg", address="789 Down St", experience="5 years", role_applied="Marketing Manager", status="Applied"),
        JobApplicant(first_name="Frank", last_name="Wright", photo="path/to/photo2.jpg", address="321 Up St", experience="3 years", role_applied="Sales Representative", status="Interviewed"),
        JobApplicant(first_name="Eva", last_name="Green", photo="path/to/photo1.jpg", address="789 Down St", experience="5 years", role_applied="Marketing Manager", status="Applied"),
        JobApplicant(first_name="Frank", last_name="Wright", photo="path/to/photo2.jpg", address="321 Up St", experience="3 years", role_applied="Sales Representative", status="Interviewed"),
        JobApplicant(first_name="Alice", last_name="Brown", photo="path/to/photo3.jpg", address="123 Park Ave", experience="2 years", role_applied="HR Coordinator", status="Applied"),
        JobApplicant(first_name="Bob", last_name="Johnson", photo="path/to/photo4.jpg", address="456 Maple Dr", experience="4 years", role_applied="Project Manager", status="Rejected"),
        JobApplicant(first_name="Carol", last_name="Davis", photo="path/to/photo5.jpg", address="789 Oak Ln", experience="1 year", role_applied="Accountant", status="Applied"),
        JobApplicant(first_name="David", last_name="Wilson", photo="path/to/photo6.jpg", address="135 Pine St", experience="6 years", role_applied="IT Specialist", status="Interviewed"),
        JobApplicant(first_name="Ella", last_name="Martinez", photo="path/to/photo7.jpg", address="246 Cedar Rd", experience="3 years", role_applied="Customer Service", status="Applied"),
        JobApplicant(first_name="George", last_name="Hernandez", photo="path/to/photo8.jpg", address="531 Birch Pl", experience="5 years", role_applied="Product Manager", status="Rejected"),
        JobApplicant(first_name="Hannah", last_name="Lee", photo="path/to/photo9.jpg", address="678 Elm St", experience="2 years", role_applied="Graphic Designer", status="Applied"),
        JobApplicant(first_name="Ian", last_name="King", photo="path/to/photo10.jpg", address="910 Spruce Ave", experience="4 years", role_applied="Software Engineer", status="Interviewed")
    ]
    db.session.bulk_save_objects(job_applicants)

    # Interviews
    interviews = [
        Interview(time=datetime.now() + timedelta(days=1), applicant_id=1),
        Interview(time=datetime.now() + timedelta(days=2), applicant_id=3),
        Interview(time=datetime.now() + timedelta(days=5), applicant_id=5),
        Interview(time=datetime.now() + timedelta(days=7), applicant_id=7),
        Interview(time=datetime.now() + timedelta(days=9), applicant_id=9),
        Interview(time=datetime.now() + timedelta(days=10), applicant_id=11)
    ]
    db.session.bulk_save_objects(interviews)

    # Documents
    documents = [
        Document(document_type="Contract", employee_id=1),
        Document(document_type="Resume", employee_id=2),
        Document(document_type="ID Proof", employee_id=3),
        Document(document_type="Contract", employee_id=4),
        Document(document_type="Resume", employee_id=5),
        Document(document_type="ID Proof", employee_id=6),
        Document(document_type="Contract", employee_id=7),
        Document(document_type="Resume", employee_id=8),
        Document(document_type="ID Proof", employee_id=9),
        Document(document_type="Contract", employee_id=10)
    ]
    db.session.bulk_save_objects(documents)


    project_employees = [
        Project_employee(project_id=1, employee_id=1),
        Project_employee(project_id=2, employee_id=2),
        Project_employee(project_id=3, employee_id=3),
        Project_employee(project_id=4, employee_id=4),
        Project_employee(project_id=5, employee_id=5),
        Project_employee(project_id=6, employee_id=6),
        Project_employee(project_id=7, employee_id=7),
        Project_employee(project_id=8, employee_id=8),
        Project_employee(project_id=9, employee_id=9),
        Project_employee(project_id=10, employee_id=10)
    ]
    db.session.bulk_save_objects(project_employees)

    department_employees = [
        Department_employee(department_id=1, employee_id=1),
        Department_employee(department_id=2, employee_id=2),
        Department_employee(department_id=3, employee_id=3),
        Department_employee(department_id=4, employee_id=4),
        Department_employee(department_id=5, employee_id=5),
        Department_employee(department_id=6, employee_id=6),
        Department_employee(department_id=7, employee_id=7),
        Department_employee(department_id=8, employee_id=8),
        Department_employee(department_id=9, employee_id=9),
        Department_employee(department_id=10, employee_id=10)
    ]
    db.session.bulk_save_objects(department_employees)


    employees_on_leave = [
        OnLeave_employee(leave_id=1, employee_id=1),
        OnLeave_employee(leave_id=3, employee_id=3),
        OnLeave_employee(leave_id=4, employee_id=4),
        OnLeave_employee(leave_id=8, employee_id=8),
        OnLeave_employee(leave_id=9, employee_id=9),
    ]
    db.session.bulk_save_objects(employees_on_leave)

    db.session.commit()


