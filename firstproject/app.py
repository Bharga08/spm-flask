from flask import Flask
app=Flask(__name__)
@app.route('/first/<int:num>')
def home(num):
    print(type(num))
    return f'the number is {num}!'
@app.route('/second')
def second():
    return'i am  in second page'
app.run(debug=True)
@app.route('/third')
def third():
    return 'i am in third page'
app.run(debug=True,use_reloader=True)
