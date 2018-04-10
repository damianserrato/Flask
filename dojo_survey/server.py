from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def survey():
    name= request.form['name']
    email= request.form['email']
    return render_template('result.html', name=name, email=email)
@app.route('/survey')
def fillout():
    return render_template('survey.html')
app.run(debug=True)

