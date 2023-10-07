from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[
                           DataRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8, max=32)])
    confirm = PasswordField('Confirm Your Password', validators=[
                            DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')




