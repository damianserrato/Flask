from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mytoenails'
@app.route('/')
def index():
    return render_template("index.html", phrase="Hello", times=5)
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/')
@app.route('/show')
def show_user():
    return render_template('user.html', name=session['name'], email=session['email'])
app.run(debug=True)