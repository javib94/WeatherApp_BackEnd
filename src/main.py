# coding=utf-8
import requests
import json
from flask import Flask, jsonify, request, abort
from logging import debug

from sqlalchemy.sql.type_api import UserDefinedType
from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema
from flask_cors import CORS


# creating the Flask application
app = Flask(__name__)

CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/login', methods=['POST'])
def get_users():
    session = Session()
    luser = session.query(User).filter(User.username==request.get_json()['username'])
    session.close()
    for user in luser:
        new_user = UserSchema().dump(user)
        new_user['password'] = ''
        return jsonify(new_user),201
    
@app.route('/register', methods=['POST'])
def add_user():
    # mount user object
    #print("json del request", request.get_json())
    posted_user = UserSchema(only=('username', 'name', 'password', 'latitud', 'longitud')).load(request.get_json())

    user = User(**posted_user, created_by="HTTP post request")

    # persist user
    session = Session()
    session.add(user)
    session.commit()

    # return created user
    new_user = UserSchema().dump(user)
    new_user['password'] = ''
    session.close()
    return jsonify(new_user), 201

@app.route('/currentweather', methods=['POST'])
def get_current():
    #session = Session()
    #luser = session.query(User).filter(User.username==request.get_json()['username'])
    #esto servira para escribir un log de la consulta 
    userdata = request.get_json()
    api_key = "033543edb64c3da524b3a8bedf52c37c"
    print(userdata)
    lat = userdata['latitud']
    lon = userdata['longitud']
    units = "metric"
    lang = "es"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=%s&lang=%s" % (lat, lon, api_key, units, lang)

    response = requests.get(url)
    data = json.loads(response.text)
    return data, 201