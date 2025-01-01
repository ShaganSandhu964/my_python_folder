from flask import Flask

''' It creates an instance of the flask class,
which will be your WSGI(web server Gateway Interface) application.
'''
# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the best Flask course"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)