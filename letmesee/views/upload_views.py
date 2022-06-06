from flask import Blueprint, render_template, request, redirect, url_for, abort, current_app, send_from_directory, g
from letmesee.views.auth_views import login_required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os

import pandas as pd

bp = Blueprint('upload', __name__, url_prefix='/upload')

class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')

@bp.route('/')
@login_required
def index():
    return render_template('upload/index.html')

@bp.route('/', methods=['POST'])
@login_required
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['ALLOWED_EXTENSIONS']:
            abort(400)
        directory = os.path.join(current_app.config['UPLOAD_PATH'], g.user.username)
        if not os.path.exists(directory):
            os.makedirs(directory)
        uploaded_file.save(os.path.join(directory, filename))
    return redirect(url_for('upload.preview'))

@bp.route('/<filename>')
@login_required
def fetch(filename):
    directory = os.path.join('data', g.user.username)
    return send_from_directory(directory, filename)

@bp.route('/preview')
@login_required
def preview():
    try:
        directory = os.path.join(current_app.config['UPLOAD_PATH'], g.user.username)
        file = os.listdir(directory)[0]
        df = pd.read_csv(os.path.join(directory, file))
        tables = df.head(6).to_html(classes='data', header="true")
        tables = tables[:24] + '"table table-striped table-hover"' + tables[40:]
        data_info = {'df' : df,
                    'df_to_html' : [tables],
                    'num_of_rows' : df.shape[0],
                    'num_of_cols' : df.shape[1]}
    except Exception as e:
        pass
    return render_template('upload/preview.html', data_info=data_info)