from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisSecret'
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")
@app.route('/show')
def show_user():
  return render_template('user.html')
app.run(debug=True)