from flask_restx import Resource, Api, fields, reqparse
from app import api
from werkzeug.datastructures import FileStorage

ns = api.namespace('posts', description='Post operations')

post_schema = reqparse.RequestParser()

post_schema.add_argument('title', type=str, required=False, location='form', help='')
post_schema.add_argument('content', type=str, required=True, location='form', help='This is required')
post_schema.add_argument('Date', type=str, required=True, location='form', help='This is required')
post_schema.add_argument('picture', type=FileStorage, required=False, location='files', help='')



post_model = api.model('Post', {
    'id': fields.Integer(required=True, description='Post ID'),
    'title': fields.String(required=False, description='Post title'),
    'content': fields.String(required=True, description='Post content'),
    'picture': fields.Raw(required=False, description='Post picture', type='file'),
})