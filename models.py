from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    national_ID = db.Column(db.String, nullable = False)
    gender = db.Column(db.String, nullable=False)
    DOB = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String, unique = True, nullable=False)
    phone = db.Column(db.String, unique = True,nullable=False)
    address = db.Column(db.VARCHAR, nullable=False)
    role = db.Column(db.String, nullable=False)
    active_status = db.Column(db.Boolean, nullable=False)
    profile_picture = db.Column(db.VARCHAR, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)
    marital_status = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    emergency_contact = db.Column(db.String, nullable=False)

    leave_id = db.Column(db.Integer, db.ForeignKey('leaves.id'))
    department = db.Column(db.Integer, db.ForeignKey('departments.id'))

    dependants = db.relationship('Dependant', backref='employee')
    references = db.relationship('Reference', backref='employee')
    bankdetails = db.relationship('BankDetail', backref='employee')
    documents = db.relationship('Document', backref='employee')
    project_assigned = db.relationship('Project', backref='employee')


class Dependant(db.Model):
    __tablename__ = 'dependants'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))


class Reference(db.Model):
    __tablename__ = 'references'

    id = db.Column(db.Integer, primary_key=True)
    reference_name = db.Column(db.String, nullable=False)
    reference_phone = db.Column(db.String, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    

class BankDetail(db.Model):
    __tablename__ = 'bankdetails'

    id = db.Column(db.Integer, primary_key=True)
    employee_salary = db.Column(db.String, nullable=False)
    employee_account = db.Column(db.String, nullable=False)
    employee_bank = db.Column(db.String, nullable=False)
    branch_code = db.Column(db.String, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String, nullable=False)
    employees = db.relationship('Employee', backref='department')


class Manager(db.Model):
    __tablename__ = 'managers'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    projects_assigned = db.Relationship('Project', backref='manager')

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    project_status = db.Column(db.String, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id'))
    employees_assigned = db.relationship('Employee', backref='project')


class Leave(db.Model):
    __tablename__ = 'leaves'

    id = db.Column(db.Integer, primary_key=True)
    leave_from =db.Column(db.DateTime, nullable=False)
    leave_to =db.Column(db.DateTime, nullable=False)
    leave_type =db.Column(db.String, nullable=False)
    leave_letter =db.Column(db.String, nullable=False)
    employees_on_leave = db.Relationship('Employee', backref='leave')


class JobApplicant(db.Model):
    __tablename__ = 'jobapplicants'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    experience = db.Column(db.String, nullable=False)
    role_applied = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    interview = db.Relationship('Interview', backref='jobapplicant')

class Interview(db.Model):
    __tablename__ = 'interviews'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('jobapplicants.id'))

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    document_type = db.Column(db.String, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
