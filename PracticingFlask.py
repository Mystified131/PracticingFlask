from flask import Flask, request, render_template, session, redirect

from PracticeControl import proclist

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
     return redirect ('/index')

@app.route("/index", methods =['GET', 'POST'])
def index2():
    return render_template('index.html')


@app.route("/answer", methods =['GET', 'POST'])
def answer():
    anslist = []
    jarg1 = request.form["textchunk"]
    jarg2 = request.form["textchunk2"]
    jarg3 = request.form["textchunk3"]
    jarg = jarg1 + " " + jarg2 + " " + jarg3
    jarg = cgi.escape(jarg)
    anslist = proclist(jarg)
    return render_template('answer.html', honey = anslist, time = session['timestamp'])

## THE GHOST OF THE SHADOW ##

if __name__ == '__main__':
    app.run()



