import os
import uuid
from flask import request, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename

class StorageController:
    
    @staticmethod
    def get_file(filename):
        upload_folder = os.path.join(current_app.root_path, 'static/uploads')
        return send_from_directory(upload_folder, filename)