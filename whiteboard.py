from flask import Flask
import logging

app=Flask(__name__)
logging.basicConfig(level=logging.DEBUG,filename="flasklogfile")

@app.route("/")
def index():
    #app.logger.info("Index page or home page loaded")
    try:
          apple=mango + orange
    except Exception as e:
        app.logger.error(f" We found this error {e}")
    
    return "Working"

@app.route("/contactus")
def contactus():
    
    return "Welcome to contact us page"

if __name__=="__main__":
    app.run(debug=True)