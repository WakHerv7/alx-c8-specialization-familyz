from flask_restx import Resource, Api, fields, reqparse
from app import api
from app.schemas.individual import individual_response
from werkzeug.datastructures import FileStorage

ns = api.namespace('families', description='Family operations')

family_schema = reqparse.RequestParser()

family_schema.add_argument('name', type=str, required=True, location='form', help='')
family_schema.add_argument('picture', type=FileStorage, required=False, location='files', help='')
family_schema.add_argument('picture_name', type=str, required=False, location='form', help='')



family_model = api.model('Family', {
    'id': fields.Integer(required=True, description='Family ID'),    
    'name': fields.String(required=True, description='Family content'),
    'picture_name': fields.String(required=False, description='Family picture_name'),
    'picture_path': fields.String(required=False, description='Family picture_path'),
    'picture': fields.Raw(required=False, description='Family picture', type='file'),
    'members': fields.Nested(individual_response),
})