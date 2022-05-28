from flask import Blueprint, request,render_template, redirect, url_for, abort, current_app, send_from_directory
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os

class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')

upload_bp = Blueprint('upload', __name__, url_prefix='/')

#@upload.route('/analysis/')
#def head_uploaded_file():
#    pass

#@upload_bp.errorhandler(413)
#def too_large(e):
#    return "File is too large", 413

@upload_bp.route('/analysis/')
def index_analysis():
    files = os.listdir(current_app.config['UPLOAD_PATH'])
    return render_template('analysis/index.html', files=files)

@upload_bp.route('/analysis/', methods = ['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']: # 추후 검증이 안되는 경우에도 400에러 발생
            return "Invalid data", 400
        uploaded_file.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    return '', 204

@upload_bp.route('/uploads/<filename>')
#@login_required : 사용자별로 데이터를 관리하기 위해서는 login이 필요할 것 같다.
def upload(filename):
    return send_from_directory(current_app.config['UPLOAD_PATH'], filename)

# upload된 데이터가 올바른 데이터인지 검증하는 validate 함수, 추후 구현해야함