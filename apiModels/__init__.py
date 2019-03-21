from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from common.util import create_mysql_uri


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = create_mysql_uri('local')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)