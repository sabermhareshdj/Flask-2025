from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Define a registration (Sign Up) form using Flask-WTF انشاء حساب مستخدم جديد
class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField(label='Sign Up')