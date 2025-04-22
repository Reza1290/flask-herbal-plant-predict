from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.StorageController import StorageController

storage_bp = Blueprint('storage', __name__)

storage_bp.route('/storage/<filename>', methods=['GET'])(StorageController.get_file)
