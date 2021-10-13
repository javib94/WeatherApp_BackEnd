# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema
from flask_cors import CORS

# creating the Flask application
app = Flask(__name__)

CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/users')
def get_users():
    # fetching from the database
    session = Session()
    user_objects = session.query(User).all()

    # transforming into JSON-serializable objects
    schema = UserSchema(many=True)
    users = schema.dump(user_objects)

    # serializing as JSON
    session.close()
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_user():
    # mount user object
    print(request.get_json())
    posted_user = UserSchema(only=('username', 'description')).load(request.get_json())

    user = User(**posted_user, created_by="HTTP post request")

    # persist user
    session = Session()
    session.add(user)
    session.commit()

    # return created user
    new_user = UserSchema().dump(user)
    session.close()
    return jsonify(new_user), 201

