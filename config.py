import os

SECRET_KEY = os.urandom(32)

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'letmesee.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PATH = 'letmesee/data'
ALLOWED_EXTENSIONS = ['.PNG', '.csv']