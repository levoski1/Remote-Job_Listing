import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_DB_PATH = os.path.join(BASE_DIR, 'remote_jobs.db')

class config:
    SQLALCHEMY_DATABASE_URI = F'sqlite:///{SQLITE_DB_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "\\\xb5v\xb4\xb4\x80\xbbZ\xc4\xc5\x05\xe2y\xe5\xfd]\xfbj\\\xf3d'\xa3^"

