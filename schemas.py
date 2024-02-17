from models import Admin, Employee, Project, Dependant, Document, Reference, JobApplicant, Interview, Department, BankDetail, Leave, Department_employee, Project_employee, OnLeave_employee
from app import ma


class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Admin
        load_instance = True
        fields = ('id', 'first_name', 'last_name', 'email')

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "admin_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("admins"),
        }
    )

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

class DependantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Dependant
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "dependant_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("dependants"),
        }
    )

dependant_schema = DependantSchema()
dependants_schema = DependantSchema(many=True)

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Document
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "document_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("documents"),
        }
    )

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)

class ReferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Reference
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "reference_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("references"),
        }
    )

reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)

class InterviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Interview
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "interview_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("interviews"),
        }
    )

interview_schema = InterviewSchema()
interviews_schema = InterviewSchema(many=True)

class JobApplicantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= JobApplicant
        load_instance = True

    interview = ma.Nested(InterviewSchema)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "job_applicant_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("job_applicants"),
        }
    )

job_applicant_schema = JobApplicantSchema()
job_applicants_schema = JobApplicantSchema(many=True)


class BankDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= BankDetail
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "bankdetail_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("bankdetails"),
        }
    )

bankdetail_schema = BankDetailSchema()
bankdetails_schema = BankDetailSchema(many=True)

# class ManagerSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model= Manager
#         load_instance = True

#     projects_assigned = ma.Nested(ProjectSchema, many = True)


#     url = ma.Hyperlinks(
#         {
#             "self": ma.URLFor(
#                 "manager_by_id",
#                 values=dict(id="<id>")),
#             "collection": ma.URLFor("managers"),
#         }
#     )

# manager_schema = ManagerSchema()
# managers_schema = ManagerSchema(many=True)


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Employee
        load_instance = True

    dependants = ma.Nested(DependantSchema, many = True)
    references = ma.Nested(ReferenceSchema, many = True)
    documents = ma.Nested(DocumentSchema, many = True)
    bankdetails = ma.Nested(BankDetailSchema)


    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "employee_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("employees"),
        }
    )

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class Department_employeeSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Department_employee
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "department_employee_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("department_employees"),
        }
    )

department_employee_schema = Department_employeeSchema()
department_employees_schema = Department_employeeSchema(many=True)


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Department
        load_instance = True

    department_employees = ma.Nested(Department_employeeSchema, many = True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "department_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("departments"),
        }
    )

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)


class Project_employeeSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Project_employee
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "project_employee_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("project_employees"),
        }
    )

project_employee_schema = Project_employeeSchema()
project_employees_schema = Project_employeeSchema(many=True)


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Project
        load_instance = True

    project_employees = ma.Nested(Project_employeeSchema, many = True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "project_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("projects"),
        }
    )

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)


class OnLeave_employeeSchema (ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Project_employee
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "employee_on_leave_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("employees_on_leave"),
        }
    )

employee_on_leave_schema = OnLeave_employeeSchema()
employees_on_leave_schema = OnLeave_employeeSchema(many=True)


class LeaveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Leave
        load_instance = True

    employees_on_leave = ma.Nested(OnLeave_employeeSchema, many = True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "leave_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("leaves"),
        }
    )

leave_schema = LeaveSchema()
leaves_schema = LeaveSchema(many=True)