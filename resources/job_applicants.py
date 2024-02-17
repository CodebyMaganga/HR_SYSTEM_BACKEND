from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, JobApplicant
from schemas import JobApplicantSchema, job_applicant_schema, job_applicants_schema

class JobApplicant_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('photo', required=True, help="photo is required")
    parser.add_argument('address', required=True, help="address is required")
    parser.add_argument('experience', required=True, help="experience is required")
    parser.add_argument('role_applied', required=True, help="role_applied is required")
    parser.add_argument('status', required=True, help="status is required")

    def get(self):
        job_applicants = JobApplicant.query.all()

        response = make_response(
            job_applicants_schema.dump(job_applicants),
            200,
        )

        return response
    
    def post(self):
        data = JobApplicant_list.parser.parse_args()
        new_job_applicant = JobApplicant(**data)

        db.session.add(new_job_applicant)
        db.session.commit()

        response = make_response(
            job_applicant_schema.dump(new_job_applicant),
            201
        )

        return response
    
class JobApplicant_by_id(Resource):
    def get(self, id):
        job_applicant = JobApplicant.query.filter_by(id=id).first()
        
        if job_applicant == None:
            response_body = {
                "error": "job_applicant does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                job_applicant_schema.dump(job_applicant),
                200,
            )

            return response
    
    def patch(self,id):
        job_applicant = JobApplicant.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(job_applicant, attr, request.get_json().get(attr))

        db.session.add(job_applicant)
        db.session.commit()


        response = make_response(
            job_applicant_schema.dump(job_applicant),
            201
        )

        return response
    
    def delete(self,id):
        job_applicant = JobApplicant.query.filter_by(id=id).first()
        db.session.delete(job_applicant)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "job_applicant data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response