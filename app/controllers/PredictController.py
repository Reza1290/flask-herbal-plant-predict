from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.models import db
from app.models.Prediction import Prediction
from app.services.models.model import predict_image
from app.utils import save_image, get_khasiat

class PredictController:

    @staticmethod
    def predict():
        if 'image' not in request.files:
            return jsonify({'msg': 'No image provided'}), 400

        file = request.files['image']
        user_id = get_jwt_identity()
        filename, filepath = save_image(file)

        label, confidence = predict_image(filepath)
        benefit = get_khasiat(label)

        pred = Prediction(
            plant_name=label + " Herbal",
            benefit=benefit,
            confidence=confidence,
            image_path=filename,
            user_id=user_id
        )
        db.session.add(pred)
        db.session.commit()

        return jsonify({
            'plant_name': label + " Herbal",
            'benefit': benefit,
            'confidence': confidence
        })

    @staticmethod
    def history():
        user_id = get_jwt_identity()
        preds = Prediction.query.filter_by(user_id=user_id).all()
        return jsonify([
            {
                'plant_name': p.plant_name,
                'benefit': p.benefit,
                'confidence': p.confidence,
                'timestamp': p.timestamp.isoformat(),
                'image_path': p.image_path
            } for p in preds
        ])
