from flask import Flask , jsonify
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from datetime import timedelta


from models import db, Interview, Dependant, Department_employee
from schemas import ma

from resources.admin import bcrypt,jwt, Admin_SignUp, Admin_Login, Admin_by_id, Admin_list
from resources.bank_details import BankDetail_list, BankDetail_by_id
from resources.department_employees import Department_employee_list, Department_employee_by_id
from resources.departments import Department_list, Department_by_id
from resources.dependants import Dependant_list, Dependant_by_id
from resources.documents import Document_list, Document_by_id
from resources.employees import Employee_list, Employee_by_id
from resources.interviews import Interview_list, Interview_by_id
from resources.job_applicants import JobApplicant_list, JobApplicant_by_id
from resources.leaves import Leave_list, Leave_by_id
from resources.on_leave_employees import OnLeaveEmployee_list, OnLeaveEmployee_by_id
from resources.project_employees import ProjectEmployee_list, Project_Employee_by_id
from resources.projects import Project_list, Project_by_id
from resources.references import Reference_list, Reference_by_id


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)



migrate =  Migrate(app, db)




db.init_app(app)
ma.init_app(app)

api=Api(app)
CORS(app)

bcrypt.init_app(app)
jwt.init_app(app)


@app.route('/')
def index():
    return "code check one two"

api.add_resource(Admin_SignUp, '/signup')
api.add_resource(Admin_Login, '/login')

api.add_resource(BankDetail_list, '/bank_details')
api.add_resource(BankDetail_by_id, '/bank_details/<int:id>')

api.add_resource(Department_employee_list, '/department_employees')
api.add_resource(Department_employee_by_id, '/department_employees/<int:id>')

api.add_resource(Department_list, '/departments')
api.add_resource(Department_by_id, '/departments/<int:id>')

api.add_resource(Dependant_list, '/dependants')
api.add_resource(Dependant_by_id, '/dependants/<int:id>')

api.add_resource(Document_list, '/documents')
api.add_resource(Document_by_id, '/documents/<int:id>')

api.add_resource(Employee_list, '/employees')
api.add_resource(Employee_by_id, '/employees/<int:id>')

api.add_resource(Interview_list, '/interviews')
api.add_resource(Interview_by_id, '/interviews/<int:id>')

api.add_resource(JobApplicant_list, '/job_applicants')
api.add_resource(JobApplicant_by_id, '/job_applicants/<int:id>')

api.add_resource(Leave_list, '/leaves')
api.add_resource(Leave_by_id, '/leaves/<int:id>')

api.add_resource(OnLeaveEmployee_list, '/on_leave_employees')
api.add_resource(OnLeaveEmployee_by_id, '/on_leave_employees/<int:id>')

api.add_resource(Project_list, '/projects')
api.add_resource(Project_by_id, '/projects/<int:id>')

api.add_resource(ProjectEmployee_list, '/project_employees')
api.add_resource(Project_Employee_by_id, '/project_employees/<int:id>')

api.add_resource(Reference_list, '/references')
api.add_resource(Reference_by_id, '/references/<int:id>')


@app.route('/interviews1')
def get_interviews():
    # Fetch all interviews from the database
    interviews = Interview.query.all()

    # Create a list to store interview data
    interview_data = []

    # Iterate over interviews and extract relevant data
    for interview in interviews:
        interview_info = {
            'id': interview.id,
            'time': interview.time,
            'applicant_first_name': interview.jobapplicant.first_name,
            "applicant_last_name": interview.jobapplicant.last_name,
            'applicant_experience':interview.jobapplicant.experience,
            'role_applied': interview.jobapplicant.role_applied
            # Add other JobApplicant attributes as needed
        }
        interview_data.append(interview_info)

    # Return the interview data as JSON
    return jsonify(interview_data)



@app.route('/dependants1')
def get_dependants():
    # Fetch all interviews from the database
    dependants = Dependant.query.all()

    # Create a list to store interview data
    dependants_data = []

    # Iterate over interviews and extract relevant data
    for dependant in dependants:
        dependant_info = {
            'id': dependant.id,
            'employee_first_name': dependant.employee.first_name,
            'employee_last_name': dependant.employee.last_name,
            'dependant_first_name': dependant.first_name,
            'dependant_last_name': dependant.last_name
            
            # 'department_employee_role':department_employee.employee.role
            # 'leave_end':department.leave.leave_to
            # Add other JobApplicant attributes as needed
        }
        dependants_data.append(dependant_info)

    # Return the interview data as JSON
    return jsonify(dependants_data)


@app.route('/department_employees1')
def get_department_employees():
    # Fetch all interviews from the database
    department_employees = Department_employee.query.all()

    # Create a list to store interview data
    department_employees_data = []

    # Iterate over interviews and extract relevant data
    for department_employee in department_employees:
        department_employee_info = {
            'id': department_employee.id,
            'employee_id': department_employee.employee.id,
            'department_name': department_employee.department.department_name,
            'employee_first_name': department_employee.employee.first_name,
            'employee_last_name': department_employee.employee.last_name
            # Add other JobApplicant attributes as needed
        }
        department_employees_data.append(department_employee_info)

    # Return the interview data as JSON
    return jsonify(department_employees_data)


if __name__ == '__main__':
    app.run(port=5555,debug=True)