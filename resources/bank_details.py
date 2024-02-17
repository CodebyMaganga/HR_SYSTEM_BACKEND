from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_jwt_extended import jwt_required

from models import db, BankDetail
from schemas import BankDetailSchema, bankdetail_schema, bankdetails_schema

class BankDetail_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('employee_salary', required=True, help="employee_salary is required")
    parser.add_argument('employee_account', required=True, help="employee_account is required")
    parser.add_argument('employee_bank', required=True, help="employee_bank is required")
    parser.add_argument('branch_code', required=True, help="branch_code is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")


    def get(self):
        bank_details = BankDetail.query.all()

        response = make_response(
            bankdetails_schema.dump(bank_details),
            200,
        )

        return response
    
    def post(self):
        data = BankDetail_list.parser.parse_args()
        new_bank_detail = BankDetail(**data)

        db.session.add(new_bank_detail)
        db.session.commit()

        response = make_response(
            bankdetail_schema.dump(new_bank_detail),
            201
        )

        return response
    
class BankDetail_by_id(Resource):
    def get(self, id):
        bank_detail = BankDetail.query.filter_by(id=id).first()
        
        if bank_detail == None:
            response_body = {
                "error": "bank_detail does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                bankdetail_schema.dump(bank_detail),
                200,
            )

            return response
    
    def patch(self,id):
        bank_detail = BankDetail.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(bank_detail, attr, request.get_json().get(attr))

        db.session.add(bank_detail)
        db.session.commit()


        response = make_response(
            bankdetail_schema.dump(bank_detail),
            201
        )

        return response
    
    def delete(self,id):
        bank_detail = BankDetail.query.filter_by(id=id).first()
        db.session.delete(bank_detail)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "bank_detail data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response