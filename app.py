"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag
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
    posts = Post.query.filter_by(user_id=user_id)
    return render_template("user.html", user=user, posts=posts)

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

@app.route("/users/<int:user_id>/posts/new")
def show_post_form(user_id):
    user = User.query.get_or_404(user_id)
    tags =Tag.query.all()
    return render_template("newpost.html", user=user, tags=tags)

@app.route("/users/<int:user_id>/posts/new", methods=['POST'])
def new_post(user_id):
    title = request.form['title']
    content = request.form['content']
    tags = request.form.getlist('tags')

    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    
    for tag in tags:
        new_tag = Tag.query.get_or_404(tag)
        posttag = PostTag(post_id=post.id, tag_id=new_tag.id)
        db.session.add(posttag)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    tag = post.connect
    tags = []
    for i in range(len(tag)):
        temp_tag = post.connect[i]
        t_id = temp_tag.tag_id
        t = Tag.query.get_or_404(t_id)
        tags.append(t)
    
    return render_template("post.html", post=post, user=user, tags=tags)

@app.route("/posts/<int:post_id>/edit")
def show_edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    
    return render_template("editpost.html", post=post, user=user)

@app.route("/posts/<int:post_id>/edit", methods=['POST'])
def edit_post(post_id):
    title = request.form['title']
    content = request.form['content']

    p = Post.query.filter_by(id=post_id)
    p.update({'title': title, 'content': content})
    db.session.commit()
    return redirect(f"/posts/{post_id}")

@app.route("/posts/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    db.session.delete(post)
    db.session.commit()
    return redirect(f"/users/{user.id}")

@app.route("/tags")
def show_tags():
    tags = Tag.query.all()
    return render_template("tags.html", tags=tags)

@app.route("/tags/new")
def new_tag_form():
    return render_template("newtag.html")

@app.route("/tags/new", methods=['POST'])
def new_tag():
    name = request.form['name']

    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()

    return redirect("/tags")

@app.route("/tags/<int:tag_id>")
def tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    post = tag.connect
    posts = []
    for i in range(len(post)):
        temp_post = tag.connect[i]
        p_id = temp_post.post_id
        p = Post.query.get_or_404(p_id)
        posts.append(p)
    return render_template("tag.html", tag=tag, posts=posts)