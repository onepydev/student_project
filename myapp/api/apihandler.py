from flask import Blueprint,request
from myapp import app
from flask_restful import Api,Resource
from  flask_jwt_extended import   JWTManager

from  myapp.api.resources.student_management import ManageStudent,AddStudent,FetchStudent,FetchOneStudent,FetchStudentPagination
from myapp.api.resources.admin_management import AdminRegistration,AdminLogin,AdminLogout

app.config['JWT_BLACKLIST_ENABLED']=True

apiview=Blueprint("apiview",__name__)
api=Api(apiview)
jwt=JWTManager(app)

#@jwt.token_in_blocklist_loader
#def check_if_token_revoked(jwt_header,jwt_payload)


api.add_resource(AddStudent,"/addstudent/")
api.add_resource(FetchStudent,"/fetchstudents/")
api.add_resource(FetchOneStudent,"/fetchstudents/<string:username>")
api.add_resource(FetchStudentPagination,"/fetchstudentspagination/<int:page>")
api.add_resource(ManageStudent,"/managestudent/<string:username>")

##Admin Endpoints##
api.add_resource(AdminRegistration,"/registeradmin")
api.add_resource(AdminLogin,"/adminlogin")
api.add_resource(AdminLogout,"/adminlogout")
