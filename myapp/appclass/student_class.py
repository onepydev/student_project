from myapp import db
from myapp.models import Students


class StudentClass():
    
    def AddStudent(self,data):
        """ This method  will add a new student  to our database """
        """  Check to ensure incoming registration email data does not  exists already"""
        
        checkEmailAndUsername=db.session.query(Students.username)\
        .filter((Students.email==data['email']) | (Students.username==data['username'])).first()
        ## select  username from students  where   (email=:email or username=:username)  #
        
        if checkEmailAndUsername:
            return {"status":2,"message":"Email or username already registered ","code":409}
        
        else:
            
            try:
                newStudent=Students()
                newStudent.fname=data['fname']
                newStudent.sname=data['sname']
                newStudent.email=data['email']
                newStudent.student_class=data['studentclass']
                newStudent.username=data['username']
                db.session.add(newStudent)
                db.session.commit()  ### finally save to database 
            
            except Exception as e:
                ### log to file here ##
                print(e)
                return {"status":2,"message":f"An error occured  while adding {data['fname']} {data['sname']} to  student table","code":500}
            else:
                return {"status":1,"message":f"You have successfully  added {data['fname']} {data['sname']}  to student table","code":200}
            
    
    
    def FetchAllStudents(self):
        """This method will fetch all the student from the database""" 
        
        try :
            AllStudents=db.session.query(Students.fname,Students.sname,Students.email,Students.username).all()
            
        except Exception as e:
            ###  Write to file ##
            print(e)
            return {"status":2,"message":" An error occured  while fetching students","code":500}
        else:
            all_students=[]
            
            if not AllStudents:
                return {"status":2,"message":"No student found","code":404}
            else:
                
                for i in AllStudents:
                    ## query
                    all_students.append(i._asdict())
                
                return {"status":1,"message":"All student successfully returned ","data":all_students,"code":200}
    
    
    def GetOneStudent(self,username):
        """ This method will fetch just one student"""
        
        try:
            fetchOneStudent=db.session.query(Students.fname,Students.sname,Students.email,Students.username)\
            .filter(Students.username==username).first()
        except Exception as e:
            print(e)
            return {"status":2,"message":" An error occured  while fetching pne students","code":500}
        else:
            if not fetchOneStudent:
                return {"status":2,"message":"No student found","code":404}
            else:
                return {"status":1,"message":"One student found","data":fetchOneStudent._asdict(),"code":200}
            
            
    def  FetchWithPage(self,page,per_page):
        """This method will fetch all the student from the database with pagination""" 
        
        try :
            AllStudents=db.session.query(Students.fname,Students.sname,Students.email,Students.username)\
            .order_by(Students.id.desc())\
            .paginate(page=page,per_page=per_page,error_out=False)
            
        except Exception as e:
            ###  Write to file ##
            print(e)
            return {"status":2,"message":" An error occured  while fetching students","code":500}
        else:
            all_students=[]
            
            if not AllStudents:
                return {"status":2,"message":"No student found","code":404}
            else:
                
                for i in AllStudents.items:
                    ## query
                    all_students.append(i._asdict())
                
                return {"status":1,"message":"All student successfully returned ","data":all_students,"code":200}
            
    def UpdateStudent(self,data,username):
        checkUser=db.session.query(Students.username).filter(Students.username==username).first()

        if not checkUser:
            return {"status":2,"message":"No student found","code":404}
        
        else:
            try:
                Students.query.filter_by(username=username).update(data)
                db.session.commit()
            except Exception as e:
                print(e)
                return {"status":2,"message":"Eror found","code":500}
            else:
                return {"status":1,"message":"Record successfully updated","code":200}
            
    def DeleteStudent(self,username):
        checkUser=db.session.query(Students.username).filter(Students.username==username).first()

        if not checkUser:
            return {"status":2,"message":"No student found","code":404}
        else:
            
            try:
                Students.query.filter_by(username=username).delete()
                ## delete from student  where username=:username 
                db.session.commit() 
            except Exception as e:
                print(e)
                return {"status":2,"message":"Eror found","code":500}
            else:
                return {"status":1,"message":"Student record successfully deleted","code":200}
            