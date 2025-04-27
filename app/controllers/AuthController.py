from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import db
from app.models.User import User
from datetime import timedelta

class AuthController:

    @staticmethod
    def register():
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'msg': 'Username already exists'}), 400

        hashed_pw = generate_password_hash(data['password'])
        new_user = User(username=data['username'], password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        expires_delta = timedelta(days=1)
        access_token = create_access_token(identity=str(new_user.id), expires_delta=expires_delta)
        return jsonify({'access_token': access_token}), 201

    @staticmethod
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if not user or not check_password_hash(user.password_hash, data['password']):
            return jsonify({'msg': 'Invalid credentials'}), 401
        expires_delta = timedelta(days=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires_delta)
        return jsonify({'access_token': access_token})
