from flask_restx import Resource, Api, fields, reqparse
from app import api
from werkzeug.datastructures import FileStorage

ns = api.namespace('likes', description='Like operations')

like_schema = reqparse.RequestParser()

like_schema.add_argument('liked_by_id', type=int, required=True, location='form', help='This is required')
like_schema.add_argument('post_id', type=int, required=True, location='form', help='This is required')

like_model = api.model('Like', {
    'id': fields.Integer(required=True, description='Like ID'),
    'liked_by_id': fields.Integer(required=True, description='liked_by ID'),
    'post_id': fields.Integer(required=True, description='Post ID'),
    # 'created_at': fields.String(required=True, description='Date content'),   
})
