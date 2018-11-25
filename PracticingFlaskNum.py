from flask import Flask, request, render_template, session, redirect

from PracticeControlNum import proclist

import datetime, os, cgi

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)

@app.route("/", methods =['GET'])
def index():
     right_now = datetime.datetime.now().isoformat()
     list = []

     for i in right_now:
        if i.isnumeric():
           list.append(i)

     tim = "".join(list)
     session['timestamp'] = tim
     return redirect ('/index2')

@app.route("/index2", methods =['GET', 'POST'])
def index2():
    return render_template('index2.html')

@app.route("/answer", methods =['GET', 'POST'])
def answer():
    error = ""
    anslist = []
    jarg1 = request.form["textchunk"]
    jarg2 = request.form["textchunk2"]
    jarg3 = request.form["textchunk3"]
    jarg1 = cgi.escape(jarg1)
    jarg2 = cgi.escape(jarg2)
    jarg3 = cgi.escape(jarg3)
    for elem in jarg1:
          if elem.isnumeric():
              error = ""
          else:    
              error = "Please use integers only."
              return render_template ('/index2.html', error = error)
    for elem in jarg2:
          if elem.isnumeric():
              error = ""
          else:    
              error = "Please use numbers only."
              return render_template ('/index2.html', error = error)
    for elem in jarg3:
          if elem.isnumeric():
              error = ""
          else:    
              error = "Please use numbers only."
              return render_template ('/index2.html', error = error)
    num1 = int(jarg1)
    num2 = int(jarg2)
    num3 = int(jarg3)
    anslist = proclist(num1, num2, num3)
    return render_template('answer2.html', honey = anslist, time = session['timestamp'])

## THE GHOST OF THE SHADOW ##

if __name__ == '__main__':
    app.run()



