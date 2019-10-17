from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore ,Security

class Config:
    SQLALCHEMY_DATABASE_URI='sqlite:///security.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='5990d3fa8ebdf59e4407adf691e1eee3'


app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)

#models
roles_users=db.Table('roles_users',
    db.Column('user_id',db.Integer(),db.ForeignKey('user.id')), 
    db.Column('role_id',db.Integer(),db.ForeignKey('role.id'))
)

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    email=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.String(255))
    active=db.Column(db.Boolean())
    confirmed_at=db.Column(db.DateTime())


class Role(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(40))
    description=db.Column(db.String(255))

user_datastore=SQLAlchemyUserDatastore(db,User,Role)
security=Security(app,user_datastore)
