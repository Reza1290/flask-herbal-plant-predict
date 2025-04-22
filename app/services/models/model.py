import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('app/services/models/data/modelku.keras',
                                #    compile=False nyalain kalo mau optimizer
                                   )
class_names = [
    'Daun Jambu Biji',
    'Daun Kunyit',
    'Daun Pepaya',
    'Daun Sirih',
    'Daun Sirsak'
]

def predict_image(path): 
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)[0]
    idx = np.argmax(pred)
    return class_names[idx], float(pred[idx])
