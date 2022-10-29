
from flask import request
from myapp.api.apimodels import AdminRegisterValidate,AdminloginWithEmail
from marshmallow.exceptions import ValidationError
from flask_restful import Resource
from myapp.appclass.admin_class import AdminClass
from flask_jwt_extended import  get_jwt,jwt_required

class AdminRegistration(Resource):
    def post(self):
        json_data=request.get_json()
        
        if not json_data:
            return {"status":2,"message":"Invalid request"},400
        
        try:
            AdminRegisterValidate().load(json_data)
        except ValidationError as err:
             return err.message,400
         
        Admin=AdminClass()
        response=Admin.AdminRegister(
            fname=json_data['fname'],
            sname=json_data['sname'],
            email=json_data['email'],
            password=json_data['password'],
            username=json_data['username'],
        )
        
        return response,response['code']
    
class  AdminLogin(Resource):
    def post(self):
        json_data=request.get_json()
        
        if not json_data:
            return {"status":2,"message":"Invalid request"},400
        
        try:
            AdminloginWithEmail().load(json_data)
        except ValidationError as err:
             return err.message,400
         
        Admin=AdminClass()
        response=Admin.AdminLogin(json_data['username'],json_data['password'])
        return response,response['code']

class AdminLogout(Resource):
    @jwt_required()
    def post(self):
        jti=get_jwt()["jti"]
        print("The JTI is ",jti)
        Admin=AdminClass()
        response=Admin.Adminlogout(jti)
        return response,response['code']