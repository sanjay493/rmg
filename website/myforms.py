from email.policy import default
from random import choices
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, TextAreaField,
                     IntegerField, BooleanField, EmailField, DateField, SelectField, PasswordField)
from wtforms.validators import InputRequired, Length, AnyOf, Email, EqualTo
from wtforms import validators, SubmitField


class DlyProduction(FlaskForm):
    rpt_date = DateField('Report Date', format='%Y-%m-%d',
                         validators=[InputRequired('Please pick up Report Date from Date dropdown')])
    unit = SelectField('Your Unit', choices=[
                       'BOL', 'BAR', 'TAL', 'KAL', 'KRB', 'MBR', 'GUA', 'MPR', 'KTR', 'BGM'], validators=[InputRequired('Please select Unit name from drop down Option')])
    shift = SelectField('Shift', choices=[
                        'A', 'B', 'C', 'T'], default='T', validators=[InputRequired('Select Shift Select T for the day final Report')])
    rm = IntegerField('ROM', default=0)
    ob = IntegerField('OB', default=0)
    lump = IntegerField('Lump', default=0)
    fines = IntegerField('Fines', default=0)
    rm_trips = IntegerField('ROM Trips', default=0)
    ob_trips = IntegerField('OB Trips', default=0)
    drill = IntegerField('Drill', default=0)


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(
        'Email is required'), Email(), Length(min=5, max=35)])
    password = PasswordField('password', validators=[InputRequired(
        'Password is required!')])


class SignupForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(
        'Email is required'), Email(), Length(min=5, max=35)])
    firstname = StringField('First Name', validators=[
                            InputRequired('First name is Required'), Length(min=5, max=35)])
    password = PasswordField('Password', validators=[InputRequired(
        'Password is required!'), Length(min=6, max=10), EqualTo('password1', message='Passwords must match')])
    password1 = StringField('Password(Confirm)', validators=[
                            InputRequired('Password is required!')])
