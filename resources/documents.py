from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Document
from schemas import DocumentSchema, document_schema, documents_schema

class Document_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('document_type', required=True, help="document_type is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")

    def get(self):
        documents = Document.query.all()

        response = make_response(
            documents_schema.dump(documents),
            200,
        )

        return response
    
    def post(self):
        data = Document_list.parser.parse_args()
        new_document = Document(**data)

        db.session.add(new_document)
        db.session.commit()

        response = make_response(
            document_schema.dump(new_document),
            201
        )

        return response
    
class Document_by_id(Resource):
    def get(self, id):
        document = Document.query.filter_by(id=id).first()
        
        if document == None:
            response_body = {
                "error": "document does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                document_schema.dump(document),
                200,
            )

            return response
    
    def patch(self,id):
        document = Document.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(document, attr, request.get_json().get(attr))

        db.session.add(document)
        db.session.commit()


        response = make_response(
            document_schema.dump(document),
            201
        )

        return response
    
    def delete(self,id):
        document = Document.query.filter_by(id=id).first()
        db.session.delete(document)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "document data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response