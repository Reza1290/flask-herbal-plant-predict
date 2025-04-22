from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.models import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['BASE_URL'] = 'http://localhost:5000'
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/herbal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret'

    db.init_app(app)
    JWTManager(app)

    from app.routes.auth import auth_bp
    from app.routes.predict import predict_bp
    from app.routes.storage import storage_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(storage_bp)


    with app.app_context():
        db.create_all()

    return app
