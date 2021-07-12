from flask import Flask,request, redirect, url_for, render_template,session,escape
import sqlite3
from trainers import Trainer

from flask.helpers import make_response
app=Flask(__name__)
@app.route('/') 
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    user={
        "username":"Maggy",
        "password":12345
         } 
    username= request.form ['username']
    password=request.form['password'] 
    if username == 'Maggy':
        if password =='12345':
            resp =make_response(redirect (url_for('scores')))
            resp.set_cookie('scores_system_username',username)
            return resp
           
    
        
    return "Wrong credentials" +str(username)

@app.route('/scores') 
def scores():
    username=request.cookies.get('scores_system_username')
    if username == None:
        return redirect (url_for('index'))
    exams =[{"subjectname":"python",
             "marks":100,
             "date": "13-july-2021"},
             {
                 "subjectname":"english",
                 "marks":98,
                 "date":"13-Jan-2021"},
             {
                 "subjectname":"java",
                 "marks":88,
                 "date":"13-Feb-2021" }    
             ]
    
    return   render_template  ('scores.html' ,scores=exams ,username=username)
         
if __name__=='__main__':
    app.run(debug=True)                 

             
