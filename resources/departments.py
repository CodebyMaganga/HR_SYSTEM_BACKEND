from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Department
from schemas import DepartmentSchema, department_schema, departments_schema

class Department_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('department_name', required=True, help="department_name is required")
    parser.add_argument('department_employees', required=True, help="department_employees is required")

    def get(self):
        departments = Department.query.all()

        response = make_response(
            departments_schema.dump(departments),
            200,
        )

        return response
    
    def post(self):
        data = Department_list.parser.parse_args()
        new_department = Department(**data)

        db.session.add(new_department)
        db.session.commit()

        response = make_response(
            department_schema.dump(new_department),
            201
        )

        return response
    
class Department_by_id(Resource):
    def get(self, id):
        department = Department.query.filter_by(id=id).first()
        
        if department == None:
            response_body = {
                "error": "department does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                department_schema.dump(department),
                200,
            )

            return response
    
    def patch(self,id):
        department = Department.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(department, attr, request.get_json().get(attr))

        db.session.add(department)
        db.session.commit()


        response = make_response(
            department_schema.dump(department),
            201
        )

        return response
    
    def delete(self,id):
        department = Department.query.filter_by(id=id).first()
        db.session.delete(department)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "department data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response