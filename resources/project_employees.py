from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Project_employee
from schemas import Project_employeeSchema, project_employee_schema, project_employees_schema

class ProjectEmployee_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('project_id', required=True, help="project_id is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")


    def get(self):
        project_employees = Project_employee.query.all()

        response = make_response(
            project_employees_schema.dump(project_employees),
            200,
        )

        return response
    
    def post(self):
        data = ProjectEmployee_list.parser.parse_args()
        new_project_employee = Project_employee(**data)

        db.session.add(new_project_employee)
        db.session.commit()

        response = make_response(
            project_employee_schema.dump(new_project_employee),
            201
        )

        return response
    
class Project_Employee_by_id(Resource):
    def get(self, id):
        project_employee = Project_employee.query.filter_by(id=id).first()
        
        if project_employee == None:
            response_body = {
                "error": "project_employee does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                project_employee_schema.dump(project_employee),
                200,
            )

            return response
    
    def patch(self,id):
        project_employee = Project_employee.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(project_employee, attr, request.get_json().get(attr))

        db.session.add(project_employee)
        db.session.commit()


        response = make_response(
            project_employee_schema.dump(project_employee),
            201
        )

        return response
    
    def delete(self,id):
        on_leave_employee = Project_employee.query.filter_by(id=id).first()
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