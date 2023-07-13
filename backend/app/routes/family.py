from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api, app
from werkzeug.utils import secure_filename
from app.models import db
from app.models.family import Family
from app.schemas.family import ns, family_schema, family_model
import json, os, time, random
from PIL import Image

date_format = "%Y-%m-%d"
document_root = app.config['UPLOAD_FOLDER']
families_root = app.config['UPLOAD_FOLDER']+'/familes'

# ns = api.namespace('families', description='Family operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class FamilyList(Resource):
    @ns.doc('list_families')
    @ns.marshal_list_with(family_model)
    def get(self):
        families = Family.query.all()
        return [family.to_dict() for family in families]

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class FamilyDetails(Resource):
    @ns.doc('get_family')
    @ns.marshal_with(family_schema)
    def get(self, id):
        family = Family.query.get(id)
        if family:
            return family.to_dict()
        return {"error": "Family not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class FamilyCreate(Resource):
    @ns.doc('create_family')
    @ns.expect(family_schema)
    @ns.marshal_with(family_schema, code=201)
    def post(self):
        args = family_schema.parse_args()

        name = args['name']
        picture = args['picture']

        family = Family(name=name,)

        if picture:
            # filename = secure_filename(picture.filename)
            # picture.save(os.path.join(families_root, filename))
            # return {'message': 'File uploaded successfully', 'filename': filename}, 201
            timestr = time.strftime("%Y%m%d-%H%M%S")
            photoName = 'Photo-'+timestr+".jpg"                
            pathToConvertedFiles = os.path.join(families_root, 'photos', photoName)
            relativePathToConvertedFiles = os.path.join('photos', photoName)
            img = Image.open(picture)
            img = img.convert('RGB')
            img.thumbnail((1024, 1024))
            img.save(pathToConvertedFiles)

            family.picture_name = photoName 
            family.picture_path = pathToConvertedFiles
            
        
        family.save()

        return family.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class FamilyUpdate(Resource):
    @ns.doc('update_family')
    @ns.expect(family_schema)
    @ns.marshal_with(family_schema)
    def put(self, id):
        if not id or id != 0:
            family = Family.query.get(id)
            if family:
                args = family_schema.parse_args()
                name = args['name']
                picture = args['picture']
                picture_name = args['picture_name']
                family.name = name
                
                if picture:
                    # Delete the old file if it exists
                    old_filename = picture_name
                    if old_filename and os.path.exists(os.path.join(families_root, old_filename)):
                        os.remove(os.path.join(families_root, old_filename))
                    
                    timestr = time.strftime("%Y%m%d-%H%M%S")
                    photoName = 'Photo-'+timestr+".jpg"                
                    pathToConvertedFiles = os.path.join(families_root, 'photos', photoName)
                    relativePathToConvertedFiles = os.path.join('photos', photoName)
                    img = Image.open(picture)
                    img = img.convert('RGB')
                    img.thumbnail((1024, 1024))
                    img.save(pathToConvertedFiles)

                    family.picture_name = photoName 
                    family.picture_path = pathToConvertedFiles
                
                db.session.commit()
                return family.to_dict()
        return {"error": "Invalid ID"}, 400

# DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class FamilyDelete(Resource):
    @ns.doc('delete_family')
    @ns.response(204, 'Family deleted')
    def delete(self, id):
        if not id or id != 0:
            family = Family.query.get(id)
            if family:
                db.session.delete(family)
                db.session.commit()
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500
