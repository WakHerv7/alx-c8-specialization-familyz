from flask_restx import Resource, Api, fields
from app import api

signup_schema = api.model('UserSignup', {
    'name': fields.String(required=True, description='Your name'),
    'email': fields.String(required=True, description='Your email'),
    'password': fields.String(required=True, description='Your password'),
    'birthdate': fields.String,
    'birthplace': fields.String,
    'telephone': fields.String,
    'profession': fields.String,
    'country': fields.String,
    'city': fields.String,
})

signin_schema = api.model('UserSignin', {
    'email': fields.String(required=True, description='Your email'),
    'password': fields.String(required=True, description='Your password'),
})