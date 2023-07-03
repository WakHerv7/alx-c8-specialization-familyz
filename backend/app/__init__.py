from flask import Flask, jsonify
from app.config import Config
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from app.models import db
# from app.routes.entry import entry_bp
from flask_restx import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

api = Api(app)
CORS(app)

app.config.from_object(Config)

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


from app.routes import entry




