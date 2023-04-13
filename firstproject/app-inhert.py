from flask import Flask,render_template,redirect,url_for,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('base1.html')
@app.route('/home')
def child():
    return render_template ('child.html')
app.run(use_reloader=True)
