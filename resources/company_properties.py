from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, CompanyProperty
from schemas import CompanyPropertySchema, company_property_schema, company_properties_schema

class CompanyProperty_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('category', required=True, help="category is required")
    parser.add_argument('brand', required=True, help="brand is required")
    parser.add_argument('description', required=False, help="description is required")
    parser.add_argument('condition', required=True, help="condition is required")
    parser.add_argument('serial_number', required=True, help="serial_number is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")

    def get(self):
        company_properties = CompanyProperty.query.all()

        response = make_response(
            company_properties_schema.dump(company_properties),
            200,
        )

        return response
    
    def post(self):
        data = CompanyProperty_list.parser.parse_args()
        new_company_property = CompanyProperty(**data)

        db.session.add(new_company_property)
        db.session.commit()

        response = make_response(
            company_property_schema.dump(new_company_property),
            201
        )

        return response
    
class CompanyProperty_by_id(Resource):
    def get(self, id):
        company_property = CompanyProperty.query.filter_by(id=id).first()
        
        if company_property == None:
            response_body = {
                "error": "company_property does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                company_property_schema.dump(company_property),
                200,
            )

            return response
    
    def patch(self,id):
        company_property = CompanyProperty.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(company_property, attr, request.get_json().get(attr))

        db.session.add(company_property)
        db.session.commit()


        response = make_response(
            company_property_schema.dump(company_property),
            201
        )

        return response
    
    def delete(self,id):
        company_property = CompanyProperty.query.filter_by(id=id).first()
        db.session.delete(company_property)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "company_property data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response