from flask import Flask,render_template,request,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
import test
app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('i1.html')






if __name__ == '__main__':
   app.run(host='0.0.0.0')