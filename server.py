from flask import Flask,render_template,request,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
import test
app = Flask(__name__)
@app.route('/')
def hello_world():
   return render_template('i1.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    from utils import admin
    if request.method == 'POST':
        nm = request.form['nm']
        pd = request.form['pd']
        if admin.loginau(nm,pd):
            return "login success"
        else:
            return "login fail"

    return render_template('index.html')




@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        # 字符串
        goodid = request.form['id']
        goodname = request.form['name']
        goodprice = request.form['price']
        goodcontain = request.form['contain']

        # DAO 数据接触
        from utils import good
        good.addgoods(goodid,goodname,goodprice,goodcontain)

        # 存照片
        f =request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path=os.path.join('/tmp/flask/upload',secure_filename(f.filename))
        f.save(upload_path)
        sudoPassword = 'Zxh991103'
        command = 'mv /tmp/flask/upload/'+secure_filename(f.filename)+'  /var/www/html/photo'+goodid+'.jpg'
        str = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        print(str)
        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
   app.run(host='0.0.0.0')