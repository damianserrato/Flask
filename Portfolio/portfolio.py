from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/about')
def about_me():
    return render_template('aboutme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
    
app.run(debug=True)