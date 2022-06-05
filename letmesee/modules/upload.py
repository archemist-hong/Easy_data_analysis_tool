from flask import Blueprint, request,render_template, redirect, url_for, abort, current_app, send_from_directory
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint('upload', __name__, url_prefix='/analysis/')

@upload_bp.route('/', methods = ['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '': 
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']: # 확장자가 다르면 400 Error
            return "Invalid data", 400
        else: # 문제 없는 경우
            file = os.path.join(current_app.config['UPLOAD_PATH'], filename) # file의 full 경로
            uploaded_file.save(file)
            return redirect(url_for('show_after_uploaded_page', file))
    return '', 204

@upload_bp.route('/<file>')
def show_after_uploaded_page(file):
    return render_template('analysis/index.html', file = file)

@upload_bp.route('/uploads/<file>')
def fetch(file):
    return send_from_directory('data', file)

# upload된 데이터가 올바른 데이터인지 검증하는 validate 함수, 추후 구현해야함