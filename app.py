from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(150), nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

# class Admin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(150), nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

#     def __repr__(self):
#         return f'<Admin {self.email}>'

# class CompanyAdmin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(150), nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

#     def __repr__(self):
#         return f'<User {self.email}>'

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Float, nullable=False, default=0.0)
#     count = db.Column(db.Integer, nullable=False, default=0)

#     def __repr__(self):
#         return f'<Product price={self.price}, count={self.count}>'
 

    
# def create_admin():
    
#     new_admin = CompanyAdmin(
#         full_name='Soban Ahmad',
#         email="soban@gmail.com",
#         password='soban123'
#     )
#     db.session.add(new_admin)
#     db.session.commit()
#     print('Admin created successfully')
      
# def update_user_email(user_id, new_email):
#     # Query the user by user_id
#     user = User.query.get(user_id)

#     # Check if the user exists
#     if user:
#         # Update the email
#         user.email = new_email
#         db.session.commit()
#         print("Email updated successfully.")
#     else:
#         print("User not found.")


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
        return render_template("quize_page.html", respons = 0)
    return redirect(request.url)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
        # create_admin()      
        # update_user_email(user_id=1, new_email="kiltar@gmail.com")

    app.run(debug=True)