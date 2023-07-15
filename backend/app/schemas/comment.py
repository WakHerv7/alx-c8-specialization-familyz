from flask_restx import Resource, Api, fields, reqparse
from app import api
from app.schemas.post import author_model, post_model
from werkzeug.datastructures import FileStorage

ns = api.namespace('comments', description='Comment operations')

comment_schema = reqparse.RequestParser()

comment_schema.add_argument('content', type=str, required=True, location='form', help='This is required')
comment_schema.add_argument('author_id', type=int, required=True, location='form', help='This is required')
comment_schema.add_argument('post_id', type=int, required=True, location='form', help='This is required')

comment_model = api.model('Comment', {
    'id': fields.Integer(required=True, description='Comment ID'),
    'content': fields.String(required=True, description='Comment content'),
    'author_id': fields.Integer(required=True, description='Author ID'),
    'post_id': fields.Integer(required=True, description='Post ID'),
    'created_at': fields.String(required=True, description='Date content'),    
    'author': fields.Nested(author_model),
    'post': fields.Nested(post_model),
})
