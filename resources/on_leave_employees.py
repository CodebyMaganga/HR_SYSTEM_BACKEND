from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, OnLeave_employee
from schemas import OnLeave_employeeSchema, employee_on_leave_schema, employees_on_leave_schema

class OnLeaveEmployee_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('leave_id', required=True, help="leave_id is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")


    def get(self):
        on_leave_employees = OnLeave_employee.query.all()

        response = make_response(
            employees_on_leave_schema.dump(on_leave_employees),
            200,
        )

        return response
    
    def post(self):
        data = OnLeaveEmployee_list.parser.parse_args()
        new_on_leave_employee = OnLeave_employee(**data)

        db.session.add(new_on_leave_employee)
        db.session.commit()

        response = make_response(
            employee_on_leave_schema.dump(new_on_leave_employee),
            201
        )

        return response
    
class OnLeaveEmployee_by_id(Resource):
    def get(self, id):
        on_leave_employee = OnLeave_employee.query.filter_by(id=id).first()
        
        if on_leave_employee == None:
            response_body = {
                "error": "on_leave_employee does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                employee_on_leave_schema.dump(on_leave_employee),
                200,
            )

            return response
    
    def patch(self,id):
        on_leave_employee = OnLeave_employee.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(on_leave_employee, attr, request.get_json().get(attr))

        db.session.add(on_leave_employee)
        db.session.commit()


        response = make_response(
            employee_on_leave_schema.dump(on_leave_employee),
            201
        )

        return response
    
    def delete(self,id):
        on_leave_employee = OnLeave_employee.query.filter_by(id=id).first()
        db.session.delete(on_leave_employee)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "on_leave_employee data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response