import os
import uuid
from flask import current_app

def save_image(file):
    ext = file.filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    filepath = path
    return filename, filepath

KHASIAT = {
    'Daun Jambu Biji': 'Mengobati diare dan menjaga kesehatan pencernaan.',
    'Daun Kunyit': 'Anti-inflamasi dan meningkatkan fungsi hati.',
    'Daun Pepaya': 'Meningkatkan kekebalan tubuh dan membantu pencernaan.',
    'Daun Sirih': 'Antiseptik alami, menyembuhkan luka dan bau mulut.',
    'Daun Sirsak': 'Membantu melawan sel kanker dan menurunkan tekanan darah.'
}

def get_khasiat(nama_daun):
    return KHASIAT.get(nama_daun, 'Khasiat tidak ditemukan.')