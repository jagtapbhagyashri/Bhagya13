from flask import Flask,redirect,render_template,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@localhost/b11_flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="bhagya123j"

db = SQLAlchemy(app)
app.app_context().push()