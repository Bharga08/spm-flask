from flask import Flask,request,redirect,url_for,render_template,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='#45679dgdjfkfn'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='emp1'
Session(app)
mysql=MySQL(app)
@app.route('/eregistration',methods=['GET','POST'])
def registration():
    if request.method=='POST':
        empid=request.form['empid']
        ename=request.form['ename']
        erole=request.form['erole']
        mobile=request.form['mobile']
        dept=request.form['dept']
        salary=request.form['salary']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s)',(empid,ename,erole,mobile,dept,salary))
        mysql.connection.commit()
        cursor.close()
        return 'details registered!'
    return render_template('eregistration.html')
app.run(debug=True,use_reloader=True)

