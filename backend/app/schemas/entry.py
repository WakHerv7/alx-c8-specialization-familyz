from flask_restx import Resource, Api, fields
from app import api

entry_schema = api.model('Entry', {
    'id': fields.Integer(required=True, description='Entry ID'),
    'title': fields.String(required=True, description='Entry Title'),
    'description': fields.String(required=True, description='Entry Description'),
    'status': fields.Boolean(required=True, description='Entry Status')
})