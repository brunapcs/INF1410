from flask import  render_template, url_for, redirect, Blueprint
from flaskblog.Users.forms import NewUserRegistrationForm, LoginForm

usuarios = Blueprint('users', __name__)

@usuarios.route("/novousuario", methods=['GET', 'POST'])
def regUser():
    form = NewUserRegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('inicial.home'))
    else:
        print("Failed to Validate")

    return render_template('registerUser.html', title = "Novo Usuario", form = form )

@usuarios.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('inicial.home'))
    else:
        print("Failed to validade")

    return render_template('login.html', title = "Login", form = form )

