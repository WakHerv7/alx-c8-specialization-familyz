from flask_restx import Resource, Api, fields, reqparse
from app import api
from werkzeug.datastructures import FileStorage

ns = api.namespace('posts', description='Post operations')

post_schema = reqparse.RequestParser()

post_schema.add_argument('title', type=str, required=False, location='form', help='')
post_schema.add_argument('content', type=str, required=True, location='form', help='This is required')
post_schema.add_argument('author_id', type=int, required=True, location='form', help='This is required')
post_schema.add_argument('picture_name', type=str, required=False, location='form', help='')
post_schema.add_argument('picture', type=FileStorage, required=False, location='files', help='')


author_model = api.model('AuthorModel', {
    "id": fields.Integer,
    "myName": fields.String,
    "myUsername": fields.String,
    "myGender": fields.String,
    "myLifeStatus": fields.String,
    "myPhoto": fields.String,
    "myPhotoName": fields.String,
})
post_comment_model = api.model('PostComment', {
    'id': fields.Integer(required=True, description='Comment ID'),
    'content': fields.String(required=True, description='Comment content'),
    'author_id': fields.Integer(required=True, description='Comment author ID'),
    'author_name': fields.String(required=True, description='Author name'),
    'author_username': fields.String(required=True, description='Author username'),
})
post_like_model = api.model('PostLike', {
    'id': fields.Integer(required=True, description='Like ID'),
    'liked_by_id': fields.Integer(required=True, description='Like by ID'),
    'liked_by_name': fields.String(required=True, description='Author name'),
    'liked_by_username': fields.String(required=True, description='Author username'),
})

post_model = api.model('Post', {
    'id': fields.Integer(required=True, description='Post ID'),
    'title': fields.String(required=False, description='Post title'),
    'content': fields.String(required=True, description='Post content'),
    'author_id': fields.Integer(required=True, description='Author ID'),
    'author_name': fields.String(required=True, description='Author name'),
    'author_username': fields.String(required=True, description='Author username'),
    'created_at': fields.String(required=True, description='Date content'),
    'picture_name': fields.String(required=False, description='Family picture_name'),
    'picture_path': fields.String(required=False, description='Family picture_path'),
    'picture': fields.Raw(required=False, description='Post picture', type='file'),
    'author': fields.Nested(author_model),    
    "comments": fields.List(fields.Nested(post_comment_model)),
    "likes": fields.List(fields.Nested(post_like_model)),
})
