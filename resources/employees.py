from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Employee
from schemas import EmployeeSchema, employee_schema, employees_schema

class Employee_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('national_ID', required=True, help="national_ID is required")
    parser.add_argument('gender', required=False, help="gender is required")
    parser.add_argument('DOB', required=True, help="DOB is required")
    parser.add_argument('email', required=True, help="email is required")
    parser.add_argument('phone', required=True, help="phone is required")
    parser.add_argument('address', required=True, help="address is required")
    parser.add_argument('role', required=True, help="role is required")
    parser.add_argument('active_status', required=True, help="active_status is required")
    parser.add_argument('profile_picture', required=True, help="profile_picture is required")
    parser.add_argument('date_joined', required=True, help="date_joined is required")
    parser.add_argument('marital_status', required=True, help="marital_status is required")
    parser.add_argument('nationality', required=True, help="nationality is required")
    parser.add_argument('emergency_contact', required=True, help="emergency_contact is required")


    def get(self):
        employees = Employee.query.all()

        response = make_response(
            employees_schema.dump(employees),
            200,
        )

        return response
    
    def post(self):
        data = Employee_list.parser.parse_args()
        new_employee = Employee(**data)

        db.session.add(new_employee)
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