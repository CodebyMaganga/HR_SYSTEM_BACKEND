from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Employee, BankDetail, Dependant, Reference, Document
from schemas import EmployeeSchema, employee_schema, employees_schema

class Employee_list(Resource):
    employees_parser = reqparse.RequestParser()
    employees_parser.add_argument('first_name', required=True, help="first_name is required")
    employees_parser.add_argument('last_name', required=True, help="last_name is required")
    employees_parser.add_argument('national_ID', required=True, help="national_ID is required")
    employees_parser.add_argument('gender', required=False, help="gender is required")
    employees_parser.add_argument('DOB', required=True, help="DOB is required")
    employees_parser.add_argument('email', required=True, help="email is required")
    employees_parser.add_argument('phone', required=True, help="phone is required")
    employees_parser.add_argument('address', required=True, help="address is required")
    employees_parser.add_argument('role', required=True, help="role is required")
    employees_parser.add_argument('active_status', required=True, help="active_status is required")
    employees_parser.add_argument('profile_picture', required=True, help="profile_picture is required")
    employees_parser.add_argument('date_joined', required=True, help="date_joined is required")
    employees_parser.add_argument('marital_status', required=True, help="marital_status is required")
    employees_parser.add_argument('nationality', required=True, help="nationality is required")
    employees_parser.add_argument('bank_details', type = dict)
    employees_parser.add_argument('dependants', type = dict)
    employees_parser.add_argument('references', type = dict)
    employees_parser.add_argument('documents', type = dict)

    bank_details_parser = reqparse.RequestParser()
    bank_details_parser.add_argument('employee_salary', required=True, help="employee_salary is required", location = 'bank_details')
    bank_details_parser.add_argument('employee_account', required=True, help="employee_account is required", location = 'bank_details')
    bank_details_parser.add_argument('employee_bank', required=True, help="employee_bank is required", location = 'bank_details')
    bank_details_parser.add_argument('branch_code', required=True, help="branch_code is required", location = 'bank_details')
    bank_details_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'bank_details')

    dependants_parser = reqparse.RequestParser()
    dependants_parser.add_argument('first_name', required=True, help="first_name is required", location = 'dependants')
    dependants_parser.add_argument('last_name', required=True, help="last_name is required", location = 'dependants')
    dependants_parser.add_argument('gender', required=True, help="gender is required", location = 'dependants')
    dependants_parser.add_argument('age', required=True, help="age is required", location = 'dependants')
    dependants_parser.add_argument('relationship', required=True, help="relationship is required", location = 'dependants')
    dependants_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'dependants')

    references_parser = reqparse.RequestParser()
    references_parser.add_argument('reference_name', required=True, help="reference_name is required", location = 'references')
    references_parser.add_argument('reference_phone', required=True, help="reference_phone is required", location = 'references')
    references_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'references')

    documents_parser = reqparse.RequestParser()
    documents_parser.add_argument('document_type', required=True, help="document_type is required", location = 'documents')
    documents_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'documents')


    def get(self):
        employees = Employee.query.all()

        response = make_response(
            employees_schema.dump(employees),
            200,
        )

        return response
    
    def post(self):
        employee_data = Employee_list.employees_parser.parse_args()
        bank_details_data = Employee_list.bank_details_parser.parse_args(req = Employee_list.employees_parser)
        dependants_data = Employee_list.dependants_parser.parse_args(req = Employee_list.employees_parser)
        references_data = Employee_list.references_parser.parse_args(req = Employee_list.employees_parser)
        documents_data = Employee_list.documents_parser.parse_args(req = Employee_list.employees_parser)

        new_employee = Employee(**employee_data)
        db.session.add(new_employee)
        db.session.commit()

        new_bank_details = BankDetail(**bank_details_data, employee_id = new_employee.id )
        db.session.add(new_bank_details)
        db.session.commit()

        new_dependants = Dependant(**dependants_data, employee_id = new_employee.id)
        db.session.add(new_dependants)
        db.session.commit()

        new_references = Reference(**references_data, employee_id = new_employee.id)
        db.session.add(new_references)
        db.session.commit()    

        new_documents = Document(**documents_data, employee_id = new_employee.id)
        db.session.add(new_documents)
        db.session.commit()      

        response = make_response(
            employee_schema.dump(new_employee),
            201
        )

        return response
    
class Employee_by_id(Resource):
    def get(self, id):
        employee = Employee.query.filter_by(id=id).first()
        
        if employee == None:
            response_body = {
                "error": "employee does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                employee_schema.dump(employee),
                200,
            )

            return response
    
    def patch(self,id):
        employee = Employee.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(employee, attr, request.get_json().get(attr))

        db.session.add(employee)
        db.session.commit()


        response = make_response(
            employee_schema.dump(employee),
            201
        )

        return response
    
    def delete(self,id):
        employee = Employee.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "employee data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response