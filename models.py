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
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.VARCHAR, nullable=False)
    role = db.Column(db.String, nullable=False)
    active_status = db.Column(db.Boolean, nullable=False)
    profile_picture = db.Column(db.VARCHAR, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)
    marital_status = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    emergency_contact = db.Column(db.String, nullable=False)


class Dependant(db.Model):
    __tablename__ = 'dependants'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    relationship = db.Column(db.String, nullable=False)


class Reference(db.Model):
    __tablename__ = 'references'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    reference1_name = db.Column(db.String, nullable=False)
    reference1_phone = db.Column(db.String, nullable=False)
    reference2_name = db.Column(db.String, nullable=False)
    reference2_phone = db.Column(db.String, nullable=False)

    employee = db.relationship('Employee', backref='reference')

class BankDetail(db.Model):
    __tablename__ = 'bankdetails'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee_salary = db.Column(db.String, nullable=False)
    employee_account = db.Column(db.String, nullable=False)
    employee_bank = db.Column(db.String, nullable=False)
    branch_code = db.Column(db.String, nullable=False)

    employee = db.relationship('Employee', backref='bankdetail')

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    employee_position = db.Column(db.String, db.ForeignKey('employees.role'))

    employee=db.relationship('Employee', backref='department')

class Manager(db.Model):
    __tablename__ = 'managers'

    id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    projects_assigned = db.Relationship('Project', backref='manager')


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable=False)
    manager_id=db.Column(db.Integer, db.ForeignKey('managers.id'))
    employees_assigned = db.Column(db.Integer, db.ForeignKey('employees.id'))
    project_status = db.Column(db.String, nullable=False)

class Leave(db.Model):
    __tablename__ = 'leaves'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    leave_from =db.Column(db.DateTime, nullable=False)
    leave_to =db.Column(db.DateTime, nullable=False)
    leave_type =db.Column(db.String, nullable=False)
    leave_letter =db.Column(db.String, nullable=False)

    employees = db.Relationship('Employee', backref='leaves')

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

class Interview(db.Model):
    __tablename__ = 'interviews'

    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('jobapplicants.id'))
    time = db.Column(db.DateTime, nullable=False)

    applicants = db.Relationship('Jobapplicant', backref='interview')

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    resume = db.Column(db.String, nullable=False)
    contract_agreement = db.Column(db.String, nullable=False)

    employee = db.Relationship('Jobapplicant', backref='document')
