from flask import Flask,render_template,request,redirect,url_for
from flask import request
from werkzeug.utils import secure_filename
import os
import test
app = Flask(__name__)


# 商城界面
@app.route('/mall')
def mallindex():
   return render_template('mallindex.html')

# 管理员菜单
@app.route('/aumanage')
def managelindex():
   return render_template('manage.html')

# 用户初始选择
@app.route('/')
def index():
   return render_template('indexFor2.html')


# 管理员登录
@app.route('/aulogin', methods=['GET', 'POST'])
def login():
    from utils import admin
    if request.method == 'POST':
        nm = request.form['username']
        pd = request.form['password']
        if admin.loginau(nm,pd):
            return redirect(url_for('managelindex'))
        else:
            return "login fail"

    return render_template('aulogin.html')


# 用户登录 直接跳转到商城
@app.route('/userlogin', methods=['GET', 'POST'])
def userlogin():
    from utils import user
    if request.method == 'POST':
        nm = request.form['username']
        pd = request.form['password']
        print(nm,pd)
        if user.loginuser(nm,pd):
            return redirect(url_for('mallindex'))
        else:
            return "login fail"

    return render_template('userlogin.html')


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
   app.run(host='127.0.0.1',debug=True)