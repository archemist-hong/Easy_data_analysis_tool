"""
file : letmesee/__init__.py
"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.txt', '.PNG'] # test용 png, 나중에 지워야함, 대소문자를 구분하는 것 같으니까 보완해야함
    app.config['UPLOAD_PATH'] = 'letmesee/data'

    from .views import main_views
    from .modules import upload
    
    app.register_blueprint(main_views.main)
    app.register_blueprint(upload.upload_bp)

    return app