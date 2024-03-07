from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required
from datetime import datetime
from flask import current_app
from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

from models import db, Leave
from schemas import LeaveSchema, leave_schema, leaves_schema

class Leave_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('leave_from', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help="leave_from is required")
    parser.add_argument('leave_to', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help="leave_to is required")
    parser.add_argument('leave_type', required=True, help="leave_type is required")
    parser.add_argument('leave_letter', required=True, help="leave_letter is required")
    parser.add_argument('employee_id', required=True, help="employee_id is required")


    def get(self):
        leaves = Leave.query.all()

        response = make_response(
            leaves_schema.dump(leaves),
            200,
        )

        return response
    
    def post(self):
        try:
            args = self.parser.parse_args()
            new_leave = Leave(**args)  # Create a new Leave object with parsed arguments

            db.session.add(new_leave)
            db.session.commit()

            response = make_response(
                leave_schema.dump(new_leave),
                201
            )
            return response

        except SQLAlchemyError as e:
            current_app.logger.error(f"Database error adding leave: {str(e)}")
            response_body = {
                "error": "Failed to add leave",
                "message": "Database error"
            }
            response = make_response(
                jsonify(response_body),
                500
            )
            return response

        except Exception as e:
            current_app.logger.error(f"Error adding leave: {str(e)}")
            response_body = {
                "error": "Failed to add leave",
                "message": str(e)
            }
            response = make_response(
                jsonify(response_body),
                500
            )
            return response
class Leave_by_id(Resource):
    def get(self, id):
        leave = Leave.query.filter_by(id=id).first()
        
        if leave == None:
            response_body = {
                "error": "leave does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                leave_schema.dump(leave),
                200,
            )

            return response
    
    def patch(self,id):
        leave = Leave.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(leave, attr, request.get_json().get(attr))

        db.session.add(leave)
        db.session.commit()


        response = make_response(
            leave_schema.dump(leave),
            201
        )

        return response
    
    def delete(self,id):
        leave = Leave.query.filter_by(id=id).first()
        db.session.delete(leave)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "leave data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response