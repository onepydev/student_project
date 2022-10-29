from myapp.models import Admins,TokenBlocklist
from werkzeug.security import generate_password_hash,check_password_hash
from  myapp import db
from datetime import datetime,timedelta,timezone
from flask_jwt_extended import create_access_token


class AdminClass():

    @staticmethod
    def AdminRegister(**kwargs):
        """ use this method to  create an Admin"""
        admin=db.session.query(Admins)\
        .filter((Admins.email==kwargs.get('email')) | (Admins.username==kwargs.get('username'))).first()
        
        if admin:
            return {"status":2,"message":"An admin already exists with the provided email or username","code":409}
        
        try:
            newAdmin=Admins()
            newAdmin.fname=kwargs.get('fname')
            newAdmin.sname=kwargs.get('sname')
            newAdmin.email=kwargs.get('email')
            newAdmin.username=kwargs.get('username')
            newAdmin.password=generate_password_hash(kwargs.get('password'))
            db.session.add(newAdmin)
            db.session.commit()
                
        except Exception as e:
            print(e)
            return {"status":2,"message":"An error occured","code":500}
        
        else:
            return {"status":1,"message":"Admin successfully registered","code":200}
        
    
    @staticmethod
    def AdminLogin(username,password):
        """ This method will authnticate the admin"""
        user=db.session.query(Admins.fname,Admins.sname,Admins.username,Admins.email,Admins.id,Admins.password).filter(Admins.username==username).first()
        
        if user and check_password_hash(user.password,password):
            
            expires=timedelta(minutes=10)
            userClaims={
                "fname":user.fname,
                "sname":user.sname,
                "email":user.email
            }
            accessToken=create_access_token(
                identity=user.id,
                fresh=True,
                expires_delta=expires,
                additional_claims=userClaims
            )
            return {"status":1,"message":"Login was sucessful","access_token":accessToken,"code":200}
        else:
            return {"status":2,"message":"Invalid username or password","code":400}
        
        
    @staticmethod
    def Adminlogout(jti):
        try:
            now=datetime.now(timezone.utc)
            db.session.add(TokenBlocklist(jit=jti,created_at=now))
            db.session.commit()
        except Exception as e :
            print(e)
            return {"status":2,"message":"logout error","code":500}
        
        else:
            return {"status":1,"message":"Logout success","code":200}