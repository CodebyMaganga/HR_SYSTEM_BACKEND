from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, Dependant
from schemas import DependantSchema, dependant_schema, dependants_schema

class Dependant_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('gender', required=False, help="gender is required")
    parser.add_argument('age', required=True, help="age is required")
    parser.add_argument('relationship', required=True, help="relationship is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")

    def get(self):
        dependants = Dependant.query.all()

        response = make_response(
            dependants_schema.dump(dependants),
            200,
        )

        return response
    
    def post(self):
        data = Dependant_list.parser.parse_args()
        new_dependant = Dependant(**data)

        db.session.add(new_dependant)
        db.session.commit()

        response = make_response(
            dependant_schema.dump(new_dependant),
            201
        )

        return response
    
class Dependant_by_id(Resource):
    def get(self, id):
        dependant = Dependant.query.filter_by(id=id).first()
        
        if dependant == None:
            response_body = {
                "error": "dependant does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                dependant_schema.dump(dependant),
                200,
            )

            return response
    
    def patch(self,id):
        dependant = Dependant.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(dependant, attr, request.get_json().get(attr))

        db.session.add(dependant)
        db.session.commit()


        response = make_response(
            dependant_schema.dump(dependant),
            201
        )

        return response
    
    def delete(self,id):
        dependant = Dependant.query.filter_by(id=id).first()
        db.session.delete(dependant)
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