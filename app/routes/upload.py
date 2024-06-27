from flask import Blueprint, request, jsonify, url_for, current_app
from werkzeug.utils import secure_filename
import os
from flask_ckeditor import upload_success, upload_fail

upload_bp=Blueprint('upload_bp', __name__)

UPLOAD_FOLDER='static/imgs/'
ALLOWED_EXTENSIONS={'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'upload' not in request.files:
        return upload_fail(message='No file part')
    file = request.files['upload']
    if file.filename == '':
        return upload_fail(message='Archivo no seleccionado')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.root_path, UPLOAD_FOLDER, filename)

        # Verificar y crear el directorio si no existe
        if not os.path.exists(os.path.dirname(filepath)):
            try:
                os.makedirs(os.path.dirname(filepath))
            except OSError as exc:
                return upload_fail(message='Failed to create directory')

        file.save(filepath)
        url = url_for('static', filename='imgs/' + filename, _external=True)
        return upload_success(url, filename=filename)
    return upload_fail(message='File not allowed')