from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Reference
from schemas import ReferenceSchema, reference_schema, references_schema

class Reference_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('reference_name', required=True, help="reference_name is required")
    parser.add_argument('reference_phone', required=True, help="reference_phone is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")

    def get(self):
        references = Reference.query.all()

        response = make_response(
            references_schema.dump(references),
            200,
        )

        return response
    
    def post(self):
        data = Reference_list.parser.parse_args()
        new_reference = Reference(**data)

        db.session.add(new_reference)
        db.session.commit()

        response = make_response(
            reference_schema.dump(new_reference),
            201
        )

        return response
    
class Reference_by_id(Resource):
    def get(self, id):
        reference = Reference.query.filter_by(id=id).first()
        
        if reference == None:
            response_body = {
                "error": "reference does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                reference_schema.dump(reference),
                200,
            )

            return response
    
    def patch(self,id):
        reference = Reference.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(reference, attr, request.get_json().get(attr))

        db.session.add(reference)
        db.session.commit()


        response = make_response(
            reference_schema.dump(reference),
            201
        )

        return response
    
    def delete(self,id):
        reference = Reference.query.filter_by(id=id).first()
        db.session.delete(reference)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "reference data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response