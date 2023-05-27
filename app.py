"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def list_users():
    # users = User.query.all()
    # return render_template("userlist.html", users=users)
    '''TODO'''

@app.route("/users")
def show_users():
    '''TODO'''

@app.route("/users/new")
def add_user_form():
    '''TODO'''

@app.route("/users/new", methods=['POST'])
def add_user():
    '''TODO'''