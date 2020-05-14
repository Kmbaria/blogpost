from . import main
from flask import render_template, url_for, redirect
from .forms import BlogPostForm
from ..models import BlogPost
from .. import db

@main.route("/")
def index():


    return render_template("index.html")

@main.route("/register_blogpost")
def register():
    blog_form = BlogPostForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog_post = blog_form.blog_post.data
        email = blog_form.email.data

        blogpost = BlogPost(title = title, blog_post = blog_post, email = email)

        db.session.add(blogpost)
        db.session.commit()
    
        return redirect("main.register")
    
    title = "Register"
    return render_template("/blogs/register.html", title=title, blog_form=blog_form)