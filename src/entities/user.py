# coding=utf-8

from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Integer, Numeric
from marshmallow import Schema, fields
from sqlalchemy import Column, String
from .entity import Entity, Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Entity, Base):
    __tablename__ = 'user'
    username = Column('username', String(length=255), unique=True)
    password = Column('password', String(length=255))
    name =  Column('name',String(length=255))
    latitud = Column('latitud', Numeric(precision=10, scale= 7))
    longitud = Column('longitud', Numeric(precision=10, scale= 7))
    
    def __init__(self, username, name, password, latitud, longitud, created_by):
        Entity.__init__(self, created_by)
        self.username = username
        self.set_password(password)
        self.name = name 
        self.latitud = latitud
        self.longitud = longitud
        
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class UserSchema(Schema):
    id = fields.Number()
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    latitud = fields.Float(places=7)
    longitud = fields.Float(places=7)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
