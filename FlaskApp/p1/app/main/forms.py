from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import validators, Required, Email, EqualTo

class BlogPostForm(FlaskForm):

    title = StringField("title", validators=[Required()])
    blog_post = TextAreaField("BlogPost", validators=[Required()])
    email = StringField("Email", validators=[Required(), Email()])