from flask import Flask, jsonify
from config import Config
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from models import db
from routes.entry import entry_bp
from flask_restful import Resource, Api
from flask_swagger_ui import get_swaggerui_blueprint
import json

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

api = Api(app)
CORS(app)
app.register_blueprint(entry_bp, url_prefix='/entry')

app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')
# db = SQLAlchemy()
migrate = Migrate(app, db)

# Configure Swagger UI
SWAGGER_URL = '/swagger'
API_URL = 'http://127.0.0.1:8100/swagger.json'
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

# @app.route("/reset")
# def reset():
#     db.drop_all()
#     db.create_all()


from routes import entry


def init_db():
    db.init_app(app)
    db.app = app

if __name__ ==  '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=8100)

