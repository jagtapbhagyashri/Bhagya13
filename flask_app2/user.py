from flask_app import db,app


class User(db.Model):
 id =db.Column(db.Integer,primary_key=True)
 username =db.Column(db.String(20))
 email=db.Column(db.String(20),unique=True,nullable=False)
 password = db.Column(db.String(255),nullable=False)

with app.app_context():
    db.create_all()