import flask
from flask import Flask,render_template
myapp=Flask(__name__,template_folder='HTML')
@myapp.route('/index')
def display():
    return("<h1>Welcome to my First Webpage</h1>")
@myapp.route('/<name>')
def Hello(name):
    return(f'Hello <h1>{name}</h1> How are you doing?')
@myapp.route('/mypage')
def mypage():
    return render_template('sidhumoosewala.html')
if __name__=='__main__':
    myapp.debug=True
    myapp.run()