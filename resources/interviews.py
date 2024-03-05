from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required
from datetime import datetime

from models import db, Interview
from schemas import InterviewSchema, interview_schema, interviews_schema

class Interview_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('--time', type=lambda x: datetime.strptime(x, '%m/%d/%Y'), required=True, help="Time in the format YYYY-MM-DD")
    parser.add_argument('applicant_id', required=True, help="applicant_id is required")


    def get(self):
        interviews = Interview.query.all()

        response = make_response(
            interviews_schema.dump(interviews),
            200,
        )

        return response
    
    def post(self):
        data = Interview_list.parser.parse_args()
        new_interview = Interview(**data)

        db.session.add(new_interview)
        db.session.commit()

        response = make_response(
            interview_schema.dump(new_interview),
            201
        )

        return response
    
class Interview_by_id(Resource):
    def get(self, id):
        interview = Interview.query.filter_by(id=id).first()
        
        if interview == None:
            response_body = {
                "error": "interview does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                interview_schema.dump(interview),
                200,
            )

            return response
    
    def patch(self,id):
        interview = Interview.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(interview, attr, request.get_json().get(attr))

        db.session.add(interview)
        db.session.commit()


        response = make_response(
            interview_schema.dump(interview),
            201
        )

        return response
    
    def delete(self,id):
        interview = Interview.query.filter_by(id=id).first()
        db.session.delete(interview)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "interview data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response