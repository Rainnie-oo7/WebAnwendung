# app.py

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Konfiguration der Flask-Anwendung
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:flaskuserpassword@db:3306/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisierung der Datenbank
db = SQLAlchemy(app)

# Konfiguration des Login Managers
login_manager = LoginManager()
login_manager.init_app(app)

# User-Modell für die Datenbank
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Laden des Benutzers über die Benutzer-ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Startseite der Anwendung
@app.route('/')
def index():
    if current_user.is_authenticated:
        return f'Hello, {current_user.username}!'
    else:
        return 'Hello, guest!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
