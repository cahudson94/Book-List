#!ENV/bin/python
"""Application for book list api."""
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

PG = {
    'user': os.environ.get("DB_USER"),
    'pw': os.environ.get("DB_PASS"),
    'db': os.environ.get("DB_NAME"),
    'host': os.environ.get("DB_HOST"),
    'port': '5432',
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % PG
app.config['DEBUG'] = os.environ.get("DEBUG")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login = LoginManager(app)


@app.route('/book-list/home/', methods=['GET'])
def home():
    """Route for the home page."""
    return render_template('home.html')


@app.route('/book-list/profile/', methods=['GET'])
def profile():
    """Route for a given user profile."""
    return render_template('home.html')


@app.route('/book-list/profile/wishlist/',
           methods=['GET', 'POST', 'PUT', 'DELETE'])
def wishlist():
    """Route for a given wishlist."""
    return render_template('home.html')


@app.route('/book-list/register/', methods=['GET', 'POST'])
def register():
    """Route for registration."""
    return render_template('home.html')


@app.route('/book-list/login/', methods=['GET', 'POST'])
def login():
    """Route for login."""
    return render_template('home.html')


@app.route('/book-list/logout/', methods=['GET'])
def logout():
    """Route for logout."""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
