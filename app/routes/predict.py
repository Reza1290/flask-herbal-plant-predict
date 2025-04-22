from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.PredictController import PredictController

predict_bp = Blueprint('predict', __name__)

predict_bp.route('/predict', methods=['POST'])(jwt_required()(PredictController.predict))
predict_bp.route('/history', methods=['GET'])(jwt_required()(PredictController.history))
