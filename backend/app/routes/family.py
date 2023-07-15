from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api, app
from werkzeug.utils import secure_filename
from app.models import db
from app.models.family import Family
from app.schemas.family import ns, family_schema, family_model
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids
from app.models.individual import Individual

import json, os, time, random
from PIL import Image

date_format = "%Y-%m-%d"
document_root = app.config['UPLOAD_FOLDER']
families_root = app.config['UPLOAD_FOLDER']+'/families'

# ns = api.namespace('families', description='Family operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class FamilyList(Resource):
    @ns.doc('list_families')
    @ns.marshal_list_with(family_model)
    def get(self):
        families = Family.query.all()
        families_as_dict_list = []
        for family in families:
            familyMembers = []
            for familymb in family.members:
                #----------------------------------
                familymbFather = None
                familymbMother = None
                if familymb.parent_male_id :
                    familymbFather = Individual.query.get(familymb.parent_male_id)
                if familymb.parent_female_id :
                    familymbMother = Individual.query.get(familymb.parent_female_id)
                
                #----------------------------------
                familymbSpouses = []
                for membersp in familymb.spouses:
                    spouseObject = membersp
                    spouse = {
                        "id":spouseObject.id,
                        "name": spouseObject.name,
                        "gender": spouseObject.gender,
                        "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead),
                    }
                    familymbSpouses.append(spouse)

                member = {
                    "id":familymb.id,
                    "myPhoto": familymb.photoPath,
                    "myPhotoName": familymb.photoName,
                    "myName": familymb.name,
                    "myGender": familymb.gender,
                    "myLifeStatus": lifeStatusFrontend(familymb.dead, familymb.youngdead),
                    "father": {
                        "id": None if familymbFather == None else familymbFather.id,
                        "name": None if familymbFather == None else familymbFather.name,
                        "gender": None if familymbFather == None else familymbFather.gender,
                        "status": None if familymbFather == None else lifeStatusFrontend(familymbFather.dead, familymbFather.youngdead),
                    },
                    "mother": {
                        "id": None if familymbMother == None else familymbMother.id,
                        "name": None if familymbMother == None else familymbMother.name,
                        "gender": None if familymbMother == None else familymbMother.gender,
                        "status": None if familymbMother == None else lifeStatusFrontend(familymbMother.dead, familymbMother.youngdead),
                    },
                    
                    "spouses": familymbSpouses,
                    "birthrank": familymb.birth_rank,
                    "birthdate": familymb.birth_date,
                    "birthplace": familymb.birth_place,
                    "email": familymb.email,
                    "telephone": familymb.telephone,
                    "profession": familymb.profession,
                    "country": familymb.country,
                    "city": familymb.city,
                    "linkedin": familymb.linkedin,
                    "twitter": familymb.twitter,
                    "facebook": familymb.facebook,
                    "instagram": familymb.instagram,
                    "aboutme": familymb.aboutme,
                    "isIncomingSpouse": familymb.isIncomingSpouse,
                    "sFatherName": familymb.sFatherName,
                    "sFatherStatus": lifeStatusFrontend(familymb.sFatherDead, False),
                    "sMotherName": familymb.sMotherName,
                    "sMotherStatus": lifeStatusFrontend(familymb.sMotherDead, False),                        
                }
            
                familyMembers.append(member)
            # ############################
            family_to_dict = family.to_dict()
            family_to_dict['members'] = familyMembers
            families_as_dict_list.append(family_to_dict)
        
        return families_as_dict_list

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class FamilyDetails(Resource):
    @ns.doc('get_family')
    @ns.marshal_with(family_model)
    def get(self, id):
        family = Family.query.get(id)
        if family:
            # ############################
            familyMembers = []
            for familymb in family.members:
                #----------------------------------
                familymbFather = None
                familymbMother = None
                if familymb.parent_male_id :
                    familymbFather = Individual.query.get(familymb.parent_male_id)
                if familymb.parent_female_id :
                    familymbMother = Individual.query.get(familymb.parent_female_id)
                
                #----------------------------------
                familymbSpouses = []
                for membersp in familymb.spouses:
                    spouseObject = membersp
                    spouse = {
                        "id":spouseObject.id,
                        "name": spouseObject.name,
                        "gender": spouseObject.gender,
                        "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead),
                    }
                    familymbSpouses.append(spouse)

                member = {
                    "id":familymb.id,
                    "myPhoto": familymb.photoPath,
                    "myPhotoName": familymb.photoName,
                    "myName": familymb.name,
                    "myGender": familymb.gender,
                    "myLifeStatus": lifeStatusFrontend(familymb.dead, familymb.youngdead),
                    "father": {
                        "id": None if familymbFather == None else familymbFather.id,
                        "name": None if familymbFather == None else familymbFather.name,
                        "gender": None if familymbFather == None else familymbFather.gender,
                        "status": None if familymbFather == None else lifeStatusFrontend(familymbFather.dead, familymbFather.youngdead),
                    },
                    "mother": {
                        "id": None if familymbMother == None else familymbMother.id,
                        "name": None if familymbMother == None else familymbMother.name,
                        "gender": None if familymbMother == None else familymbMother.gender,
                        "status": None if familymbMother == None else lifeStatusFrontend(familymbMother.dead, familymbMother.youngdead),
                    },
                    
                    "spouses": familymbSpouses,
                    "birthrank": familymb.birth_rank,
                    "birthdate": familymb.birth_date,
                    "birthplace": familymb.birth_place,
                    "email": familymb.email,
                    "telephone": familymb.telephone,
                    "profession": familymb.profession,
                    "country": familymb.country,
                    "city": familymb.city,
                    "linkedin": familymb.linkedin,
                    "twitter": familymb.twitter,
                    "facebook": familymb.facebook,
                    "instagram": familymb.instagram,
                    "aboutme": familymb.aboutme,
                    "isIncomingSpouse": familymb.isIncomingSpouse,
                    "sFatherName": familymb.sFatherName,
                    "sFatherStatus": lifeStatusFrontend(familymb.sFatherDead, False),
                    "sMotherName": familymb.sMotherName,
                    "sMotherStatus": lifeStatusFrontend(familymb.sMotherDead, False),                        
                }
            
                familyMembers.append(member)
            # ############################
            family_to_dict = family.to_dict()
            family_to_dict['members'] = familyMembers
            
            return family_to_dict
        
        return {"error": "Family not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class FamilyCreate(Resource):
    @ns.doc('create_family')
    @ns.expect(family_schema)
    @ns.marshal_with(family_model, code=201)
    def post(self):
        args = family_schema.parse_args()

        name = args['name']
        picture = args['picture']

        family = Family(name=name)

        if picture:
            # filename = secure_filename(picture.filename)
            # picture.save(os.path.join(families_root, filename))
            # return {'message': 'File uploaded successfully', 'filename': filename}, 201
            timestr = time.strftime("%Y%m%d-%H%M%S")
            photoName = 'Photo-'+timestr+".jpg"                
            pathToConvertedFiles = os.path.join(families_root, photoName)
            img = Image.open(picture)
            img = img.convert('RGB')
            img.thumbnail((1024, 1024))
            img.save(pathToConvertedFiles)

            family.picture_name = photoName 
            family.picture_path = pathToConvertedFiles
        
        if args['members']:
            family_members = []
            for memberID in json.loads(args['members']):
                member = Individual.query.get(int(memberID))
                family_members.append(member)

            family.set_members(family_members)
        
        family.save()

        return family.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class FamilyUpdate(Resource):
    @ns.doc('update_family')
    @ns.expect(family_schema)
    @ns.marshal_with(family_model)
    def put(self, id):
        if not id or id != 0:
            family = Family.query.get(id)
            if family:
                args = family_schema.parse_args()
                name = args['name']
                picture = args['picture']
                
                family.name = name
                
                if picture:
                    # Delete the old file if it exists
                    old_filename = args['picture_name']
                    if old_filename and os.path.exists(os.path.join(families_root, old_filename)):
                        os.remove(os.path.join(families_root, old_filename))
                    
                    timestr = time.strftime("%Y%m%d-%H%M%S")
                    photoName = 'Photo-'+timestr+".jpg"                
                    pathToConvertedFiles = os.path.join(families_root, photoName)
                    img = Image.open(picture)
                    img = img.convert('RGB')
                    img.thumbnail((1024, 1024))
                    img.save(pathToConvertedFiles)

                    family.picture_name = photoName 
                    family.picture_path = pathToConvertedFiles
                
                if args['members']:
                    family_members = []
                    for memberID in json.loads(args['members']):
                        member = Individual.query.get(int(memberID))
                        family_members.append(member)

                    family.set_members(family_members)
                
                family.save()
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
