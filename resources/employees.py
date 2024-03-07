from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from werkzeug.utils import secure_filename
import uuid as uuid
import os
#from app import app
from flask_jwt_extended import jwt_required
from datetime import datetime

from models import db, Employee, BankDetail, Dependant, EmergencyContact, Reference, Document,CompanyProperty
from schemas import EmployeeSchema, employee_schema, employees_schema


class Employee_list(Resource):
    def get(self):
        employees = Employee.query.all()

        response = make_response(
            employees_schema.dump(employees),
            200,
        )

        return response
    
    # #a post function to allow uploading an image or file
    # def upload_file():
    #     #get access to the actual picture
    #     profile_picture = request.files['profile_picture']#profile_picture is the name in the input field on the front end
    #     #if the user has then uploaded a file or image without the name given above; the below function checks that
    #     if not profile_picture:
    #         return "No profile picture uploaded", 400
        
    #     #after getting the image, get the image name and its file.to get file names securely, import secure_filename
    #     filename = secure_filename(profile_picture.filename)

    #     employee= Employee(profile_picture=profile_picture.read())
    #     db.session.add(employee)
    #     db.session.commit()

    #     return "Profile picture has been uploaded!", 200

    def post(self):
        data = request.get_json()
        # Create new employee
        new_employee = Employee(
            first_name = data["first_name"] ,
            last_name = data["last_name"],
            DOB = datetime.strptime(data['DOB'], '%Y-%m-%d'),
            email = data["email"],
            phone = data["phone"],
            gender = data["gender"],
            national_ID =  data["national_ID"],
            address = data["address"],
            role = data["role"],
            active_status = data["active_status"],
            profile_picture = data["profile_picture"],
            nationality = data["nationality"],
            date_joined = datetime.strptime(data['date_joined'], '%Y-%m-%d'),
            marital_status = data["marital_status"],
            )
        # #after getting the image, get the image name(filename to store it in the server)
        # profile_picture = request.files['profile_picture']
        # pic_filename = secure_filename(profile_picture.filename)

        # #when users upload same image with same name; randomize the nme with uuid
        # pic_name = str(uuid.uuid1()) + "_" + pic_filename

        #  #save the image
        # saver= data["profile_picture"]
        
        # #change it to a string to save to db
        # profile_picture = pic_name

        # Handle file upload
        profile_picture = request.files.get('profile_picture')
        if profile_picture:
            # Generate a unique filename
            filename = secure_filename(profile_picture.filename)
            pic_name = str(uuid.uuid1()) + "_" + filename
            # Save the image to the upload folder
            profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            # Save the filename to the new employee record
            new_employee.profile_picture = pic_name
    


        db.session.add(new_employee)
        db.session.commit()
        #saver.save(os.path.join(app.config['UPLOAD_FOLDER']),pic_name)


        # If bank details are provided
        if 'bankdetails' in data:
            # bank_details_data = data['bankdetails']
            new_bank_details = BankDetail(
            employee_salary = data["bankdetails"]["employee_salary"],
            employee_account = data["bankdetails"]["employee_account"],
            employee_bank = data["bankdetails"]["employee_bank"],
            branch_code = data["bankdetails"]["branch_code"],
            employee_id= new_employee.id,
            )

            db.session.add(new_bank_details)
        
        # If dependants are provided
        if 'dependants' in data:
            dependants_data = data['dependants']
            new_dependants = [Dependant(
            first_name = data["dependants"]["first_name"],
            last_name = data["dependants"]["last_name"],
            gender = data["dependants"]["gender"],
            age = data["dependants"]["age"],
            relationship = data["dependants"]["relationship"], 
            employee_id=new_employee.id) for d in dependants_data]

        db.session.add_all(new_dependants)


        # If emergency_contacts are provided
        if 'emergency_contacts' in data:
            emergency_contacts_data = data['emergency_contacts']
            new_emergency_contacts = [EmergencyContact(
            first_name = data["emergency_contacts"]["first_name"],
            last_name = data["emergency_contacts"]["last_name"],
            gender = data["emergency_contacts"]["gender"],
            relationship = data["emergency_contacts"]["relationship"], 
            employee_id=new_employee.id) for d in emergency_contacts_data]

        db.session.add_all(new_emergency_contacts)

        
        # If references are provided
        if 'references' in data:
            references_data = data['references']
            new_references = [Reference(
                reference_name = data["references"]["reference_name"],
                reference_phone = data["references"]["reference_phone"],
                employee_id=new_employee.id) for r in references_data]
            
        db.session.add_all(new_references)
        
        # If documents are provided
        if 'documents' in data:
            documents_data = data['documents']
            new_documents = [Document(
                document_type = data["documents"]["document_type"],
                employee_id=new_employee.id) for d in documents_data]
            
        db.session.add_all(new_documents)
        #company property details
        if 'company_properties' in data:
            company_properties_data = data ['company_properties']
            new_company_properties = [CompanyProperty(
                category = data ['company_properties']['category'],
                brand = data ['company_properties'] ['brand'],
                description = data ['company_properties'] ['description'],
                condition = data ['company_properties'] ['condition'],
                serial_number = data ['company_properties'] ['serial_number'],
                employee_id=new_employee.id) for r in company_properties_data]
           

        db.session.add_all(new_company_properties)

        db.session.commit()

        response = make_response(
            employee_schema.dump(new_employee),
            201
        )
        return response
    

class Employee_by_id(Resource):
    def get(self, id):
        employee = Employee.query.filter_by(id=id).first()
        
        if employee == None:
            response_body = {
                "error": "employee does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                employee_schema.dump(employee),
                200,
            )

            return response
    
    def patch(self, id):
        employee = Employee.query.filter_by(id=id).first()

        for attr in request.get_json():
            setattr(employee, attr, request.get_json().get(attr))

        db.session.add(employee)
        db.session.commit()

        bank_details = BankDetail.query.filter_by(employee_id=id)
        for detail in bank_details:
            for attr in request.get_json():
                setattr(detail, attr, request.get_json().get(attr))
            db.session.add(detail)

        dependants = Dependant.query.filter_by(employee_id=id)
        for dependant in dependants:
            for attr in request.get_json():
                setattr(dependant, attr, request.get_json().get(attr))
            db.session.add(dependant)

        references = Reference.query.filter_by(employee_id=id)
        for reference in references:
            for attr in request.get_json():
                setattr(reference, attr, request.get_json().get(attr))
            db.session.add(reference)

        documents = Document.query.filter_by(employee_id=id)
        for document in documents:
            for attr in request.get_json():
                setattr(document, attr, request.get_json().get(attr))
            db.session.add(document)

        db.session.commit()

        response = make_response(
            employee_schema.dump(employee),
            201
        )

        return response
    
    def delete(self,id):
        employee = Employee.query.filter_by(id = id).first()
        bankdetails = BankDetail.query.filter_by(employee_id = id)
        dependants = Dependant.query.filter_by(employee_id = id)
        references = Reference.query.filter_by(employee_id = id)
        documents = Document.query.filter_by(employee_id = id)

        for bankdetail in bankdetails:
            db.session.delete(bankdetail)

        for dependant in dependants:
            db.session.delete(dependant)

        for reference in references:
            db.session.delete(reference)

        for document in documents:
            db.session.delete(document)

        db.session.delete(employee)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "employee data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response
    

    # def post(self):
    # Extract employee data
    
    # employee_data = data.get('employee', {})
    # print(employee_data)
    #     employee_data = Employee_list.employees_parser.parse_args()
    #     bank_details_data = Employee_list.bank_details_parser.parse_args(req = Employee_list.employees_parser.parse_args())
    #     dependants_data = Employee_list.dependants_parser.parse_args(req = Employee_list.employees_parser.parse_args())
    #     references_data = Employee_list.references_parser.parse_args(req = Employee_list.employees_parser.parse_args())
    #     documents_data = Employee_list.documents_parser.parse_args(req = Employee_list.employees_parser.parse_args())

    #     new_employee = Employee(**employee_data)
    #     db.session.add(new_employee)
    #     db.session.commit()

    #     new_bank_details = BankDetail(**bank_details_data, employee_id = new_employee.id )
    #     db.session.add(new_bank_details)
    #     db.session.commit()

    #     new_dependants = Dependant(**dependants_data, employee_id = new_employee.id)
    #     db.session.add(new_dependants)
    #     db.session.commit()

    #     new_references = Reference(**references_data, employee_id = new_employee.id)
    #     db.session.add(new_references)
    #     db.session.commit()    

    #     new_documents = Document(**documents_data, employee_id = new_employee.id)
    #     db.session.add(new_documents)
    #     db.session.commit()      

    #     response = make_response(
    #         employee_schema.dump(new_employee),
    #         201
    #     )

    #     return response



    # class Employee_list(Resource):
    # employees_parser = reqparse.RequestParser()
    # employees_parser.add_argument('first_name', required=True, help="first_name is required")
    # employees_parser.add_argument('last_name', required=True, help="last_name is required")
    # employees_parser.add_argument('national_ID', required=True, help="national_ID is required")
    # employees_parser.add_argument('gender', required=False, help="gender is required")
    # employees_parser.add_argument('DOB', required=True, help="DOB is required")
    # employees_parser.add_argument('email', required=True, help="email is required")
    # employees_parser.add_argument('phone', required=True, help="phone is required")
    # employees_parser.add_argument('address', required=True, help="address is required")
    # employees_parser.add_argument('role', required=True, help="role is required")
    # employees_parser.add_argument('active_status', required=True, help="active_status is required")
    # employees_parser.add_argument('profile_picture', required=True, help="profile_picture is required")
    # employees_parser.add_argument('date_joined', required=True, help="date_joined is required")
    # employees_parser.add_argument('marital_status', required=True, help="marital_status is required")
    # employees_parser.add_argument('nationality', required=True, help="nationality is required")
    # employees_parser.add_argument('bankdetails', type = dict, action = "append")
    # employees_parser.add_argument('dependants', type = dict, action = "append")
    # employees_parser.add_argument('references', type = dict, action = "append")
    # employees_parser.add_argument('documents', type = dict, action = "append")

    # bank_details_parser = reqparse.RequestParser()
    # bank_details_parser.add_argument('employee_salary', required=True, help="employee_salary is required", location = 'bankdetails',)
    # bank_details_parser.add_argument('employee_account', required=True, help="employee_account is required", location = 'bankdetails',)
    # bank_details_parser.add_argument('employee_bank', required=True, help="employee_bank is required", location = 'bankdetails',)
    # bank_details_parser.add_argument('branch_code', required=True, help="branch_code is required", location = 'bankdetails',)
    # # bank_details_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'bank_details')

    # dependants_parser = reqparse.RequestParser()
    # dependants_parser.add_argument('first_name', required=True, help="first_name is required", location = 'dependants',)
    # dependants_parser.add_argument('last_name', required=True, help="last_name is required", location = 'dependants',)
    # dependants_parser.add_argument('gender', required=True, help="gender is required", location = 'dependants',)
    # dependants_parser.add_argument('age', required=True, help="age is required", location = 'dependants',)
    # dependants_parser.add_argument('relationship', required=True, help="relationship is required", location = 'dependants',)
    # # dependants_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'dependants')

    # references_parser = reqparse.RequestParser()
    # references_parser.add_argument('reference_name', required=True, help="reference_name is required", location = 'references',)
    # references_parser.add_argument('reference_phone', required=True, help="reference_phone is required", location = 'references',)
    # # references_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'references')

    # documents_parser = reqparse.RequestParser()
    # documents_parser.add_argument('document_type', required=True, help="document_type is required", location = 'documents',)
    # # documents_parser.add_argument('employee_id', required=True, help="employee_id is required", location = 'documents')