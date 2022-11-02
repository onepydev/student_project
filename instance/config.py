import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI=os.environ("SQLALCHEMY_DATABASE_URI")
SECRET_KEY=os.environ("SECRET_KEY")