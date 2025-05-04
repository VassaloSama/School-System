from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000
app.config['DEBUG'] = True

# Config Banco MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:SenhaForte123@db:3306/school-system"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)