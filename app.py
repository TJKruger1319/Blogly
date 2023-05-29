"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)

@app.route("/")
def list_users():
    users = User.query.all()
    return render_template("userlist.html", users=users)


@app.route("/users")
def show_users():
    users = User.query.all()
    return render_template("userlist.html", users=users)

@app.route("/users/new")
def add_user_form():
    return render_template("add.html")

@app.route("/users/new", methods=['POST'])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route("/users/<int:user_id>")
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)

@app.route("/users/<int:user_id>/edit")
def show_edit_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)

@app.route("/users/<int:user_id>/edit", methods=['POST'])
def edit_user(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    u = User.query.filter_by(id=user_id)
    u.update({'first_name': first_name, 'last_name': last_name, 'image_url': image_url})
    db.session.commit()

    return redirect('/users')

@app.route("/users/<int:user_id>/delete", methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')