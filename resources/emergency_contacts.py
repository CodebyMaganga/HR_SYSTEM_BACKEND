from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, EmergencyContact
from schemas import EmergencyContactSchema, emergency_contacts_schema, emergency_contact_schema

class EmergencyContact_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('gender', required=False, help="gender is required")
    parser.add_argument('relationship', required=True, help="relationship is required")
    parser.add_argument('phone', required=True, help="Phone number is required")

    def get(self):
        emergency_contacts = EmergencyContact.query.all()

        response = make_response(
            emergency_contacts_schema.dump(emergency_contacts),
            200,
        )

        return response
    
    def post(self):
        data = EmergencyContact_list.parser.parse_args()
        new_emergency_contact = EmergencyContact(**data)

        db.session.add(new_emergency_contact)
        db.session.commit()

        response = make_response(
            emergency_contact_schema.dump(new_emergency_contact),
            201
        )

        return response
    
class EmergencyContact_by_id(Resource):
    def get(self, id):
        emergency_contact = EmergencyContact.query.filter_by(id=id).first()
        
        if emergency_contact == None:
            response_body = {
                "error": "emergency_contact does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                emergency_contact_schema.dump(emergency_contact),
                200,
            )

            return response
    
    def patch(self,id):
        emergency_contact = EmergencyContact.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(emergency_contact, attr, request.get_json().get(attr))

        db.session.add(emergency_contact)
        db.session.commit()


        response = make_response(
            emergency_contact_schema.dump(emergency_contact),
            201
        )

        return response
    
    def delete(self,id):
        emergency_contact = EmergencyContact.query.filter_by(id=id).first()
        db.session.delete(emergency_contact)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "dependant data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response