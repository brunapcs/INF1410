from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##sudo lsof -i:5000

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DFDEWRvr345beT234Tnu7y98iudfcdw2e32'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog.Users.routes import usuarios
from flaskblog.Main.routes import inicial

app.register_blueprint(usuarios)
app.register_blueprint(inicial)