from models import Employee, Project, Dependant, Document, Reference, JobApplicant, Interview, Department, BankDetail, Manager, Leave
from app import ma

class Employeeschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Employee

class Projectschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Project

class Dependantschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Dependant

class Documentschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Document

class Referenceschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Reference

class JobApplicantschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= JobApplicant

class Interviewschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Interview

class Departmentschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Department

class BankDetailschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= BankDetail

class Managerschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Manager

class Leaveschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Leave