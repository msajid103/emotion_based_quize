from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from data import quiz_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
@app.route('/', methods=['GET', 'POST'])
def index():    
    return render_template("index.html")

@app.route('/login_page')
def login_page():   
    return render_template("login.html")

@app.route('/quiz')
def quiz():   
    return render_template("quiz.html")

@app.route('/quiz_started', methods=['POST'])
def quiz_started():
    if 'imageUpload' not in request.files:
        return redirect(request.url)
    file = request.files['imageUpload']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the file or perform your image processing here
        file.save('./static/image.jpg')       
        return render_template("quize_page.html", respons = 1)
    return redirect(request.url)

if __name__ == '__main__': 

    app.run(debug=True)