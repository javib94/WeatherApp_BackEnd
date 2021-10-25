# coding=utf-8

from flask import Flask, jsonify, request, abort
from logging import debug
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
    # fetching from the database
    session = Session()
    #user_objects = session.query(User).filter(User.username==).filter(User.check_password())
    user_objects = session.query(User).filter(User.username=='javier@gmail.com').count()
    if (user_objects > 0): 
        #transforming into JSON-serializable objects
        schema = UserSchema(many=True)
        users = schema.dump(user_objects)
        # serializing as JSON
        session.close()
        return jsonify(users)
    # else:
    #     abort(403)

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
    session.close()
    return jsonify(new_user), 201

