from flask import Flask,request,redirect,render_template,url_for,flash,session
from flask_mysqldb import MySQL
from flask_session import Session
from otp import genotp
from cmail import sendmail
import random
app=Flask(__name__)
app.secrect_key='*67@hjyjmzk'
app.config['SESSION_TYPE']='filesystem'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='SPM'
Session(app)
mysql=MySQL(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/registration',methods=['GET','POST'])
def register():
    if request.method=='POST':
        rollno=request.form['rollno']
        name=request.form['name']
        group=request.form['group']
        password=request.form['password']
        code=request.form['code']
        email=request.form['email']
        #define college code
        ccode='sdmsmkpbsc$#23'
        if ccode==code:
            cursor=mysql.connection.cursor()
            cursor.execute('select rollno from students')
            data=cursor.fetchall()
            cursor.execute('select email from students')
            edata=cursor.fetchall()
            #print(data)
            if (rollno,) in data:
                flash('user already already exists')
                return render_template('register.html')
            if(email,) in data:
               flash('email id already already exists')
               return render_template('register.html')
            cursor.close()
            otp=genotp()
            sendmail(email,otp)
            return render_template('otp.html',otp=otp,rollno=rollno,name=name,group=group,password=password,email=email)       
        else:
            print(request.form)
            flash('Invalid college code')
            return render_template('register.html')
    return render_template('register.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method=='POST':
        rollno=request.form['id']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('select count(*) from students where rollno=%s and password=%s',[rollno,password])
        count=cursor.fetchone()[0]
        if count==0:
            flash('Invalid rollno or password')
            return render_template('login.html')
        else:
            session['user']=rollno
            return redirect(url_for('home'))
    return render_template('login.html')
@app.route('/Studenthome')
def home():
    if session.get('user'):
         return render_template('home.html')
    else:
        #implement flash
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('index'))
    else:
        flash('already logged out!')
        return redirect(url_for('login'))
@app.route('/otp/<otp>/<rollno>/<name>/<group>/<password>/<email>',methods=['GET','POST'])
def otp(otp,rollno,name,group,password,email):
    if request.method=='POST':
        uotp=request.form['otp']
        if otp==uotp:
            cursor=mysql.connection.cursor()
            lst=[rollno,name,group,password,email]
            qurey='insert into students values(%s,%s,%s,%s,%s)'
            cursor.execute(qurey,lst)
            mysql.connection.commit()
            cursor.close()
            flash('Details registered')
            return redirect(url_for('login'))
        else:
            flash('wrong otp')
            return render_template('otp.html',otp=otp,rollno=rollno,name=name,group=group,password=password,email=email)
@app.route('/noteshome')
def notehome():
    if session.get('user'):
        rollno=session.get('user')
        cursor=mysql.connection.cursor()
        cursor.execute('select * from notes where rollno=%s',[rollno])
        notes_data=cursor.fetchall()
        print(notes_data)
        cursor.close()
        return render_template('addnotetable.html',data=notes_data)
    else:
        return redirect(url_for('login'))
@app.route('/addnotes',methods=['GET','POST'])
def addnote():
    if session.get('user'):
        if request.method=='POST':
            title=request.form['title']
            content=request.form['content']
            cursor=mysql.connection.cursor()
            rollno=session.get('user')
            cursor.execute('insert into notes(rollno,title,content) values(%s,%s,%s)',[rollno,title,content])
            mysql.connection.commit()
            cursor.close()
            flash(f'{title} added successfully')
            return redirect(url_for('notehome'))
                           
        return render_template('notes.html')
    else:
        return redirect(url_for('login'))
@app.route('/viewnotes/<nid>')
def viewnote(nid):
    cursor=mysql.connection.cursor()
    cursor.execute('select title,content from notes where nid=%s',[nid])
    data=cursor.fetchone()
    return render_template('notesview.html',data=data)
@app.route('/updatenotes/<nid>')
def updatenotes(nid):
    if session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute('select title,content from notes where nid=%s',[nid])
        data=cursor.fetchone()
        cursor.close()
        if request.method=='POST':
            title=request.form['title']
            content=request.form['content']
            cursor=mysql.connection.cursor()
            cursor.excute('update notes set title=%s,content=%s where nid=%s',[title,content,nid])
            mysql.connection.commit()
            cursor.close()
            flash('notes updated successfully')
            return redirect(url_for('notehome'))
        return render_tempalte('updatenotes.html',data=data)
    else:
        return redirect(url_for('login'))
@app.route('/deletenotes/<nid>')
def deletenotes(nid):
    cursor=mysql.connection.cursor()
    cursor.execute('delete from notes where nid=%s',[nid])
    mysql.connection.commit()
    cursor.close()
    flash('notes deleted successfully')
    return redirect(url_for('noteshome'))
@app.route('/fileshome')
def fileshome():
    if session.get('user'):
        rollno=session.get('user')
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT fid,filename,data from files where rollno=%s',[rollno])
        data=cursor.fetchall()
        return render_template('fileuploadtable.html',data=data)
    else:
        return redirect(url_for('login'))
@app.route('/filehandling',methods=['POST'])
def filehandling():
    file=request.files['files']
    filename=file.filename
    bin_file=file.read()
    rollno=session.get('user')
    cursor=mysql.connection.cursor()
    cursor.execute('insert into files(rollno,filename,filedata) values(%s,%s,%s)',[rollno,filename,bin_file])
    mysql.connection.commit()
    cursor.close()
    flash(f'{filename} upload successfully')
    return redirect(url_for('filehome'))
@app.route('/viewfile/<fid>')
def viewfile(fid):
    if session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute('select filename,filedata from files where fid=%s',[fid])
        data=cursor.fetchone()
        cursor.close()
        filename=data[0]
        bin_file=data[1]
        byte_data=bytesIO(bin_file)
        return send_file(byte_data,download_name=filename,as_attachment=True)
    else:
        return redirect(url_for('login'))
@app.route('/filedelete/<fid>')
def filedelete():
    cursor=mysql.connection.cursor()
    cursor.execute('delete from files where fid=%s',[fid])
    mysql.connection.commit()
    cursor.close()
    flash('file deleted successfully')
    return redirect(url_for('fileshome'))
@app.route('/forgetpassword',methods=['GET','POST'])
def forget():
    if request.method=='POST':
        rollno=request.form['id']
        cursor=mysql.connection.cursor()
        cursor.execute('select rollno from students')
        data=cursor.fetchall()
        cursor.close()
        if(rollno,) in data:
            cursor.execute('select email  from students where rollno=%s',[rollno])
            data=cursor.fetchone()[0]
            cursor.close()
            subject=f'Reset password for {email}'
            body=f'Reset the password using-{request.host+url_for{"createpassword",token=token(rollno,120))}'
            sendmail(data,subject,body)
            flash('reset link send to ypur mail')
            return redirect(url_for('login'))
        else:
            return 'Invalid user id'
    return render_template('forget.html')
@app.route('/createpassword/<token>',methods=['GET','POST'])
def createpassword(token):
    try:
        s=Serializer(app.config['SECRET_KEY'])
        rollno=s.loads(token)['user']
        if request.method=='POST':
            npass=request.form['npassword']
            cpass=request.form['cpassword']
            if npass==cpass:
                cursor=mysql.connection.cursor()
                cursor.execute('update students set password=%s where rollno=%s',[npass,rollno])
                mysql.connection.commit()
                return 'password reset successfully'
            else:
                return 'password mismatch'
        return render_template('newpassword.html')
    except:
        return 'Link expired try again'
app.run(use_reloader=True,debug=True)
