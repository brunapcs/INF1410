from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class NewUserRegistrationForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email() ])
    password = PasswordField('senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Registrar Conta')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('senha', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Lembre-se de Mim ')
    submit = SubmitField('Login')
