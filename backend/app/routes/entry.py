from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api
from app.models import db
from app.models.entry import Entry
from app.schemas.entry import entry_schema
import json




ns = api.namespace('entries', description='Entry operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class EntryList(Resource):
    @ns.doc('list_entries')
    @ns.marshal_list_with(entry_schema)
    def get(self):
        entries = Entry.query.all()
        return [entry.to_dict() for entry in entries]

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class EntryDetails(Resource):
    @ns.doc('get_entry')
    @ns.marshal_with(entry_schema)
    def get(self, id):
        entry = Entry.query.get(id)
        if entry:
            return entry.to_dict()
        return {"error": "Entry not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class EntryCreate(Resource):
    @ns.doc('create_entry')
    @ns.expect(entry_schema)
    @ns.marshal_with(entry_schema, code=201)
    def post(self):
        data = api.payload
        title = data['title']
        description = data['description']
        status = True

        entry = Entry(title=title, description=description, status=status)
        db.session.add(entry)
        db.session.commit()

        return entry.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class EntryUpdate(Resource):
    @ns.doc('update_entry')
    @ns.expect(entry_schema)
    @ns.marshal_with(entry_schema)
    def put(self, id):
        if not id or id != 0:
            entry = Entry.query.get(id)
            if entry:
                data = api.payload
                title = data['title']
                description = data['description']
                entry.title = title
                entry.description = description
                db.session.commit()
                return entry.to_dict()
        return {"error": "Invalid ID"}, 400

# DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class EntryDelete(Resource):
    @ns.doc('delete_entry')
    @ns.response(204, 'Entry deleted')
    def delete(self, id):
        if not id or id != 0:
            entry = Entry.query.get(id)
            if entry:
                db.session.delete(entry)
                db.session.commit()
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500
