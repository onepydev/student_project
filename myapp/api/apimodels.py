
from marshmallow import fields,validate
from flask_marshmallow import Marshmallow

ma=Marshmallow()
not_blank=validate.Length(min=1,error="Field cannot be blank")

class AddStudentValidator(ma.Schema):
    fname=fields.String(required=True,validate=not_blank)
    sname=fields.String(required=True,validate=not_blank)
    email=fields.Email(required=True,validate=not_blank)
    username=fields.String(required=True,validate=not_blank)
    studentclass=fields.String(required=True,validate=not_blank)
    
class  AdminRegisterValidate(ma.Schema):
    username=fields.String(required=True,validate=not_blank)
    password=fields.String(required=True,validate=not_blank)
    email=fields.Email(required=True,validate=not_blank)
    fname=fields.String(required=True,validate=not_blank)
    sname=fields.String(required=True,validate=not_blank)
    
class AdminloginWithEmail(ma.Schema):
    username=fields.String(required=True,validate=not_blank)
    password=fields.String(required=True,validate=not_blank)