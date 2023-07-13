from flask import Flask, jsonify
from app.config import Config
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from app.models import db
# from app.routes.entry import entry_bp
from flask_restx import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
# from flask_uploads import UploadSet, configure_uploads, IMAGES

from flask_marshmallow import Marshmallow


import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))
marshmallow = Marshmallow()

app = Flask(__name__)

api = Api(app)
CORS(app)

app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['UPLOADED_PHOTOS_DEST'] = 'static/photos'
# photos = UploadSet('photos', IMAGES)

# configure_uploads(app, photos)

marshmallow.init_app(app)
migrate = Migrate(app, db)


# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Sample API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))


from app.routes import entry, individual




