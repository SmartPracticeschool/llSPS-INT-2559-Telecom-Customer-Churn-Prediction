# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:21:20 2020

@author: Mugdhama
"""


from flask import Flask,render_template , request
# name of application which will talk to html page
app=Flask(__name__)#interface btw the server and application 

import pickle
model=pickle.load(open('exit.pkl','rb'))
@app.route('/')#bind to an url
def helloworld():
    return render_template("churn2.html")
@app.route('/login',methods = ['POST'])#bind to an url
def admin():
    #p=request.form['cn']
    q=request.form['cs']
    s=request.form['s']
    if (s=="France"):
        s1,s2,s3=1,0,0
    if(s=='Germany'):
        s1,s2,s3=0,1,0
    if(s=='Spain'):
        s1,s2,s3=0,0,1
    g=request.form['g']
    if(g=="Male"):
        g1=1
    if(g=="Female"):
        g1=0
    r=request.form['age']
    a=request.form['t']
    b=request.form['b']
    c=request.form['p']
    d=request.form['c']
    if(d=="No"):
        d1=0
    if(d=="Yes"):
        d1=1
    e=request.form['ac']
    if(e=="No"):
        e1=0
    if(e=="Yes"):
        e1=1
    f=request.form['sal']
    t=[[int(s1),int(s2),int(s3),int(q),int(g1),int(r),int(a),int(b),int(c),int(d1),int(e1),int(f)]]
    y=model.predict(t)
    index=["No","Yes"]
    o=index[y[0]]
    return render_template("churn2.html", y="Customer will exit ? :"+o)


if __name__== '__main__':
    app.run(debug=True)#means that while the program is running,the modification made will not be rendered in the app
    #if debug=True, we cannot directly run the code from sypder. we have to run code from anaconda prompt
    