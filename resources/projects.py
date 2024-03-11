from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Project
from schemas import ProjectSchema, project_schema, projects_schema

class Project_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help="title is required")
    parser.add_argument('project_status', required=True, help="project_status is required")

    @jwt_required()
    def get(self):
        projects = Project.query.all()

        response = make_response(
            projects_schema.dump(projects),
            200,
        )

        return response
    
    @jwt_required()
    def post(self):
        data = Project_list.parser.parse_args()
        new_project = Project(**data)

        db.session.add(new_project)
        db.session.commit()

        response = make_response(
            project_schema.dump(new_project),
            201
        )

        return response
    
class Project_by_id(Resource):
    
    @jwt_required()
    def get(self, id):
        project = Project.query.filter_by(id=id).first()
        
        if project == None:
            response_body = {
                "error": "project does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                project_schema.dump(project),
                200,
            )

            return response
        
    @jwt_required()
    def patch(self,id):
        project = Project.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(project, attr, request.get_json().get(attr))

        db.session.add(project)
        db.session.commit()


        response = make_response(
            project_schema.dump(project),
            201
        )

        return response
    
    @jwt_required()
    def delete(self,id):
        project = Project.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "project data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response