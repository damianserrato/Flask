from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    print "Name " + name
    print "Email " + email

    return redirect('/')
app.run(debug=True)