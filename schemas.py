from models import Admin, Employee, Project, Dependant, EmergencyContact, Document, Reference, JobApplicant, Interview, Department, BankDetail, Leave, CompanyProperty
from flask_marshmallow import Marshmallow

ma= Marshmallow()


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
            "collection": ma.URLFor("admin_list"),
        }
    )

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

class DependantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Dependant
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('dependants',))    

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "dependant_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("dependant_list"),
        }
    )

dependant_schema = DependantSchema()
dependants_schema = DependantSchema(many=True)

class EmergencyContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= EmergencyContact
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('emergency_contacts',))    

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "emergencycontact_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("emergencycontact_list"),
        }
    )

emergency_contact_schema = EmergencyContactSchema()
emergency_contacts_schema = EmergencyContactSchema(many=True)

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Document
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('documents',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "document_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("document_list"),
        }
    )

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)

class ReferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Reference
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('references',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "reference_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("reference_list"),
        }
    )

reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)

class InterviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Interview
        load_instance = True
        include_fk = True

    jobapplicant = ma.Nested(lambda: JobApplicantSchema, many = False, exclude = ('interview',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "interview_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("interview_list"),
        }
    )

interview_schema = InterviewSchema()
interviews_schema = InterviewSchema(many=True)

class JobApplicantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= JobApplicant
        load_instance = True

    interview = ma.Nested( InterviewSchema, many = False, exclude = ('jobapplicant',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "jobapplicant_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("jobapplicant_list"),
        }
    )

job_applicant_schema = JobApplicantSchema()
job_applicants_schema = JobApplicantSchema(many=True)


class BankDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= BankDetail
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('bankdetails',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "bankdetail_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("bankdetail_list"),
        }
    )

bankdetail_schema = BankDetailSchema()
bankdetails_schema = BankDetailSchema(many=True)


class CompanyPropertySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= CompanyProperty
        load_instance = True
        include_fk = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('company_properties',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "companyproperty_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("companyproperty_list"),
        }
    )

company_property_schema = CompanyPropertySchema()
company_properties_schema = CompanyPropertySchema(many=True)


class LeaveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Leave
        load_instance = True

    employee = ma.Nested(lambda: EmployeeSchema, many = False, exclude = ('leave',))

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "leave_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("leave_list"),
        }
    )

leave_schema = LeaveSchema()
leaves_schema = LeaveSchema(many=True)



class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Employee
        include_fk = True
        load_instance = True

    
    leave = ma.Nested(LeaveSchema, many = False, exclude = ('employee',))
    dependants = ma.Nested(DependantSchema, many = True, exclude = ('employee',))
    references = ma.Nested(ReferenceSchema, many = True, exclude = ('employee',))
    documents = ma.Nested(DocumentSchema, many = True, exclude = ('employee',))
    bankdetails = ma.Nested(BankDetailSchema, many = True, exclude = ('employee',))
    company_properties = ma.Nested(CompanyPropertySchema, many = True, exclude = ('employee',))
    emergency_contacts = ma.Nested(EmergencyContactSchema, many = True, exclude = ('employee',))



    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "employee_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("employee_list"),
        }
    )

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Department
        load_instance = True

    department_employees = ma.Nested(EmployeeSchema, many = True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "department_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("department_list"),
        }
    )

department_schema = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)


class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Project
        load_instance = True

    project_employees = ma.Nested(EmployeeSchema, many = True)

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "project_by_id",
                values=dict(id="<id>")),
            "collection": ma.URLFor("project_list"),
        }
    )

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

