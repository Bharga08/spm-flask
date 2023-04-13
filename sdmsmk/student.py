from flask import Flask,request,redirect,url_for,render_template,session
from flask_session import Session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key='#45679dgdjfkfn'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='student'
Session(app)
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def registration():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        course=request.form['course']
        address=request.form['address']
        mobile=request.form['mobile']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into students values(%s,%s,%s,%s,%s)',(id1,name,course,address,mobile))
        mysql.connection.commit()
        cursor.close()
        return 'details registered!'
    return render_template('registration.html')
app.run(debug=True,use_reloader=True)
