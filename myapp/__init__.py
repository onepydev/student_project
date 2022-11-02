from email.mime import application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

app=Flask(__name__,instance_relative_config=True)
app.config.from_pyfile("config.py") ## import configa
db=SQLAlchemy(app)
migrate=Migrate(app,db)

logging.basicConfig(
       level=logging.DEBUG,
      filename="applogs.log"
      ) 


from myapp import models
from  .api.apihandler import apiview

app.logger.debug("What a great program")
app.register_blueprint(apiview,url_prefix="/api")
