from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Department_employee
from schemas import Department_employeeSchema, department_employee_schema, department_employees_schema

class Department_employee_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('department_id', required=True, help="department_id is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")

    def get(self):
        department_employees = Department_employee.query.all()

        response = make_response(
            department_employees_schema.dump(department_employees),
            200,
        )

        return response
    
    def post(self):
        data = Department_employee_list.parser.parse_args()
        new_department_employee = Department_employee(**data)

        db.session.add(new_department_employee)
        db.session.commit()

        response = make_response(
            department_employee_schema.dump(new_department_employee),
            201
        )

        return response
    
class Department_employee_by_id(Resource):
    def get(self, id):
        department_employee = Department_employee.query.filter_by(id=id).first()
        
        if department_employee == None:
            response_body = {
                "error": "department_employee does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                department_employee_schema.dump(department_employee),
                200,
            )

            return response
    
    def patch(self,id):
        department_employee = Department_employee.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(department_employee, attr, request.get_json().get(attr))

        db.session.add(department_employee)
        db.session.commit()


        response = make_response(
            department_employee_schema.dump(department_employee),
            201
        )

        return response
    
    def delete(self,id):
        department_employee = Department_employee.query.filter_by(id=id).first()
        db.session.delete(department_employee)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "department_employee data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response