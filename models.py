"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)


class User(db.Model):
    """Users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    first_name = db.Column(db.String(30),
                           nullable=False)
    last_name = db.Column(db.String(30),
                          nullable=False)
    image_url = db.Column(db.Text)

class Post(db.Model):
    """Posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(60),
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))
    users = db.relationship('User', backref='posts')

    connect = db.relationship('PostTag', backref='post')


class Tag(db.Model):
     """Tags"""

     __tablename__ = "tags"

     id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
     name = db.Column(db.Text,
                      nullable=False)
     connect = db.relationship('PostTag', backref='tag')
     
class PostTag(db.Model):
     """Mapping a tag to a post"""

     __tablename__ = "posttag"

     post_id = db.Column(db.Integer, 
                       db.ForeignKey('posts.id'),
                       primary_key=True)
     tag_id = db.Column(db.Integer, 
                       db.ForeignKey('tags.id'),
                       primary_key=True)
     

