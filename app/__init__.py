import os
from flask import Flask

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)),'uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
