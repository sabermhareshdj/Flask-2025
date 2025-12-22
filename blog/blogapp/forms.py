from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from blogapp.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

# Define a registration (Sign Up) form using Flask-WTF انشاء حساب مستخدم جديد
class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField(label='Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username already exist')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email already exist')
        

#
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message='Enter Your Email'), Email(message='Invalid email address')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField(label="Remember me")
    submit = SubmitField(label='Sign In') # 


class UpdateProfileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    profile_picture = FileField(label="Update Profole Picture", validators=[FileAllowed(['png','jpg'], message="only png and jpg files are allowed")])
    submit = SubmitField(label='Update')

    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('username already exist')
        
    def validate_email(self, email):
        if email.data != current_user.email: 
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('email already exist')
