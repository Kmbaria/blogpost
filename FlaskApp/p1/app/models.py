from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blogposts = db.relationship("BlogPost", backref="users", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("cannot access the password attribute")

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self, password):
        check_password_hash(self.pass_secure, password)


class BlogPost(db.Model):
    __tablename__ = "blogpost"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    blog_post = db.Column(db.String(255))
    email=db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def get_all_posts(cls):
        blog = BlogPost.query.all()
        return blog

    @classmethod
    def get_single_post(cls,blogpost):
        blog = BlogPost.query.filter_by(id=blog_post)
        return blog
    
    @classmethod
    def get_users_blogs(cls,user_id):
        blog=BlogPost.query.filter_by(users_id=user_id)
        return blog
