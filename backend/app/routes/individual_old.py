from flask import Blueprint, request, redirect, jsonify, render_template, send_from_directory
# from flask import Flaskfrom flask import send_from_directory
from flask_restx import Resource, Api, fields, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app import api, app
from app.models import db
from app.helpers import lifeValue, create_individual, process_parents, process_generations
from app.models.individual import Individual
from app.schemas.individual import individual_schema
import json, os, time
from PIL import Image



ns = api.namespace('individuals', description='Individual operations')

upload_parser = reqparse.RequestParser()
# upload_parser.add_argument('file', location='files', type=FileStorage, required=True)
upload_parser.add_argument('title', type=str, required=True, location='form', help='Title is required')
upload_parser.add_argument('description', type=str, required=True, location='form', help='Description is required')
upload_parser.add_argument('picture', type=bytes, required=True, location='files', help='Picture is required')

document_root = app.config['UPLOAD_FOLDER']

@api.route('/upload')
class UploadFile(Resource):
    @ns.doc('upload_post')
    @api.expect(upload_parser)
    def post(self):
        # args = upload_parser.parse_args()
        # file = args['file']
        args = upload_parser.parse_args()
        title = args['title']
        description = args['description']
        picture = args['picture']
        if picture:
            filename = secure_filename(picture.filename)
            picture.save(os.path.join(document_root, filename))
            return {'message': 'File uploaded successfully', 'filename': filename}, 201

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(document_root, filename)

# LIST ALL ---------------------------------------
# @api.route('/upload')
# class UploadFile(Resource):
#     @ns.doc('list_uploads')
#     @ns.marshal_list_with(upload_parser)
#     def get(self):
#         uploads = UploadFile.query.all()
#         return uploads
#         # return [upload.to_dict() for upload in uploads]

# ===========================================================================================
# ===========================================================================================

@ns.route('/')
class NewFamilyMember(Resource):
    @ns.doc('new_family_member')
    @api.expect(individual_schema)
    # @ns.marshal_with(individual_schema, code=201)
    def post(self):
        args = upload_parser.parse_args()
        
        currentMemberId = args['currentMemberId']
        urlLastButOneItem = args['urlLastButOneItem']
        myName = args['myName']
        myGender = args['myGender']
        myLifeStatus = args['myLifeStatus']
        isIncomingSpouse = args['isIncomingSpouse']
        noPhotoCheck = args['noPhotoCheck']
        uploadedPhotoName = args['uploadedPhotoName']
        uploadedPhoto = args['uploadedPhoto'] if uploadedPhotoName != 'undefined' else False
        fatherId = args['fatherId']
        newFatherCheck = args['newFatherCheck']
        newFatherName = args['newFatherName']
        hasFatherCheck = args['hasFatherCheck']
        fatherLifeStatusValue = args['fatherLifeStatusValue']
        motherId = args['motherId']
        newMotherCheck = args['newMotherCheck']
        newMotherName = args['newMotherName']
        hasMotherCheck = args['hasMotherCheck']
        motherLifeStatusValue = args['motherLifeStatusValue']
        spouseValues = args['spouseValues']
        birthdate = args['birthdate']
        birthplace = args['birthplace']
        birthrank = args['birthrank']
        email = args['email']
        telephone = args['telephone']
        profession = args['profession']
        country = args['country']
        city = args['city']
        linkedin = args['linkedin']
        twitter = args['twitter']
        facebook = args['facebook']
        instagram = args['instagram']
        aboutme = args['aboutme']

        
        if hasMotherCheck == False and newMotherCheck != True :
            motherId = None
        my_lv = lifeValue(myLifeStatus)

        # Modify family member
    #     if currentMemberId != 'null' and urlLastButOneItem == 'update_item':
    #         cmo = Individual.query.get(currentMemberId)
    #         cmo.name = myName
    #         cmo.gender = myGender
    #         cmo.dead = my_lv["dv"]
    #         cmo.youngdead = my_lv["ydv"]
    #         cmo.generation = None
    #         cmo.parent_male_id = fatherId
    #         cmo.parent_female_id = motherId
    #         cmo.birth_rank = None if birthrank == '' else birthrank
    #         cmo.birth_date = None if birthdate == '' else birthdate
    #         cmo.birth_place = birthplace
    #         cmo.email = email
    #         cmo.telephone = telephone
    #         cmo.profession = profession
    #         cmo.country = country
    #         cmo.city = city
    #         cmo.linkedin = linkedin
    #         cmo.twitter = twitter
    #         cmo.facebook = facebook
    #         cmo.instagram = instagram
    #         cmo.aboutme = aboutme
    #         if cmo.isIncomingSpouse :
    #             cmo.sFatherName = newFatherName
    #             cmo.sMotherName = newMotherName
    #             mlv = lifeValue(motherLifeStatusValue)
    #             flv = lifeValue(fatherLifeStatusValue)
    #             cmo.sFatherDead = flv["dv"]
    #             cmo.sMotherDead = mlv["dv"]
    #         if noPhotoCheck:
    #             cmo.photoName = None
    #             cmo.photoPath.delete()
    #         else:
    #             if uploadedPhoto:
    #                 if cmo.photoPath:
    #                     cmo.photoPath.delete()                
    #                 timestr = time.strftime("%Y%m%d-%H%M%S")
    #                 photoName = 'Photo-'+timestr+".jpg"                
    #                 pathToConvertedFiles = os.path.join(document_root,'photos', photoName)
    #                 relativePathToConvertedFiles = os.path.join('photos', photoName)
    #                 img = Image.open(uploadedPhoto)
    #                 img = img.convert('RGB')
    #                 img.thumbnail((256, 256))
    #                 img.save(pathToConvertedFiles)                
    #                 cmo.photoName = photoName
    #                 cmo.photoPath.name = relativePathToConvertedFiles
    #         # ######################
    #         SVs = []
    #         for sve in json.loads(spouseValues):
    #             if sve["newConjointCheck"] == True:
    #                 lv = lifeValue(sve["status"])
    #                 indiv = Individual(
    #                     name = sve["newConjointName"],
    #                     gender = sve["gender"],
    #                     dead = lv["dv"],
    #                     youngdead = lv["ydv"]
    #                 )
    #                 indiv.save()
    #                 SVs.append(indiv.id)
    #             else:
    #                 SVs.append(int(sve["conjointId"]))
    #         cmo.spouses.set(SVs)            
    #         cmo.save()
    #         # ######################
    #     else:
    #         # ... (rest of the code remains the same)
    #          # Create a new family member
    #         fm = Individual(
    #             name = myName,
    #             gender = myGender,
    #             dead = my_lv["dv"],
    #             youngdead = my_lv["ydv"],
    #             generation = None,
    #             parent_male_id = fatherId,
    #             parent_female_id = motherId,
    #             birth_rank = None if birthrank == '' else birthrank,
    #             birth_date = None if birthdate == '' else birthdate,
    #             birth_place = birthplace,
    #             email = email,
    #             telephone = telephone,
    #             profession = profession,
    #             country = country,
    #             city = city,
    #             linkedin = linkedin,
    #             twitter = twitter,
    #             facebook = facebook,
    #             instagram = instagram,
    #             aboutme = aboutme,
    #             isIncomingSpouse = False if isIncomingSpouse == False else True,                             
    #         )
    #         if urlLastButOneItem == 'new_spouse' :
    #             fm.isIncomingSpouse = True
    #             fm.sFatherName = newFatherName
    #             fm.sMotherName = newMotherName
    #             mlv = lifeValue(motherLifeStatusValue)
    #             flv = lifeValue(fatherLifeStatusValue)
    #             fm.sFatherDead = flv["dv"]
    #             fm.sMotherDead = mlv["dv"]            
    #         if not(noPhotoCheck) and uploadedPhoto:
    #             timestr = time.strftime("%Y%m%d-%H%M%S")
    #             photoName = 'Photo-'+timestr+".jpg"
    #             pathToConvertedFiles = os.path.join(document_root,'photos', photoName)
    #             relativePathToConvertedFiles = os.path.join('photos', photoName)
    #             img = Image.open(uploadedPhoto)
    #             img = img.convert('RGB')
    #             img.thumbnail((256, 256))
    #             img.save(pathToConvertedFiles)
    #             fm.photoName = photoName
    #             fm.photoPath.name = relativePathToConvertedFiles                
    #         fm.save()      
    #         # ######################
    #         SVs = []
    #         for sv in json.loads(spouseValues):
    #             if sv["newConjointCheck"] == True:
    #                 lv = lifeValue(sv["status"])
    #                 indiv = Individual(
    #                     name = sv["newConjointName"],
    #                     gender = sv["gender"],
    #                     dead = lv["dv"],
    #                     youngdead = lv["ydv"]
    #                 )
    #                 indiv.save()
    #                 SVs.append(indiv.id)
    #             else:
    #                 SVs.append(int(sv["conjointId"]))
    #         fm.spouses.set(SVs)
    #         fm.save()
    # sdsd
        return {"message": "Success"}, 200



# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class IndividualUpdate(Resource):
    @ns.doc('update_individual')
    @api.expect(individual_schema)
    # @ns.marshal_with(individual_schema)
    def put(self, id):
        args = individual_schema.parse_args()        
        currentMemberId = args['currentMemberId']
        urlLastButOneItem = args['urlLastButOneItem']
        myName = args['myName']
        myGender = args['myGender']
        myLifeStatus = args['myLifeStatus']
        isIncomingSpouse = args['isIncomingSpouse']
        noPhotoCheck = False if args['noPhotoCheck'] == False else True
        uploadedPhotoName = args['uploadedPhotoName']
        uploadedPhoto = args['uploadedPhoto'] if uploadedPhotoName != 'undefined' else False
        fatherId = args['fatherId']
        newFatherCheck = args['newFatherCheck']
        newFatherName = args['newFatherName']
        hasFatherCheck = args['hasFatherCheck']
        fatherLifeStatusValue = args['fatherLifeStatusValue']
        motherId = args['motherId']
        newMotherCheck = args['newMotherCheck']
        newMotherName = args['newMotherName']
        hasMotherCheck = args['hasMotherCheck']
        motherLifeStatusValue = args['motherLifeStatusValue']
        spouseValues = args['spouseValues']
        birthdate = args['birthdate']
        birthplace = args['birthplace']
        birthrank = args['birthrank']
        email = args['email']
        telephone = args['telephone']
        profession = args['profession']
        country = args['country']
        city = args['city']
        linkedin = args['linkedin']
        twitter = args['twitter']
        facebook = args['facebook']
        instagram = args['instagram']
        aboutme = args['aboutme']

        my_lv = lifeValue(myLifeStatus)
        fatherId = process_parents(hasFatherCheck, newFatherCheck, urlLastButOneItem, fatherId, newFatherName, fatherLifeStatusValue, 'm')
        motherId = process_parents(hasMotherCheck, newMotherCheck, urlLastButOneItem, motherId, newMotherName, motherLifeStatusValue, 'f')      

        cmo = Individual.query.get(currentMemberId)
        cmo.name = myName
        cmo.gender = myGender
        cmo.dead = my_lv["dv"]
        cmo.youngdead = my_lv["ydv"]
        cmo.generation = None
        cmo.parent_male_id = fatherId
        cmo.parent_female_id = motherId
        cmo.birth_rank = None if birthrank == '' else birthrank
        cmo.birth_date = None if birthdate == '' else birthdate
        cmo.birth_place = birthplace
        cmo.email = email
        cmo.telephone = telephone
        cmo.profession = profession
        cmo.country = country
        cmo.city = city
        cmo.linkedin = linkedin
        cmo.twitter = twitter
        cmo.facebook = facebook
        cmo.instagram = instagram
        cmo.aboutme = aboutme
        if cmo.isIncomingSpouse :
            cmo.sFatherName = newFatherName
            cmo.sMotherName = newMotherName
            mlv = lifeValue(motherLifeStatusValue)
            flv = lifeValue(fatherLifeStatusValue)
            cmo.sFatherDead = flv["dv"]
            cmo.sMotherDead = mlv["dv"]
        if noPhotoCheck:
            cmo.photoName = None
            cmo.photoPath = None
        else:
            if uploadedPhoto:
                # Delete the old file if it exists
                old_filename = request.args.get('old_filename')
                if old_filename and os.path.exists(os.path.join(document_root, old_filename)):
                    os.remove(os.path.join(document_root, old_filename))

                # Save the new file
                timestr = time.strftime("%Y%m%d-%H%M%S")
                photoName = 'Photo-'+timestr+".jpg"                
                pathToConvertedFiles = os.path.join(document_root,'photos', photoName)
                relativePathToConvertedFiles = os.path.join('photos', photoName)
                img = Image.open(uploadedPhoto)
                img = img.convert('RGB')
                img.thumbnail((256, 256))
                img.save(pathToConvertedFiles)                
                cmo.photoName = photoName
                cmo.photoPath = relativePathToConvertedFiles

                # new_filename = secure_filename(uploadedPhoto.filename)
                # uploadedPhoto.save(os.path.join(document_root, new_filename))
                # return {'message': 'File updated successfully', 'filename': new_filename}, 200

        # ######################
        
        SVs = []
        for sve in json.loads(spouseValues):
            if sve["newConjointCheck"] == True:
                lv = lifeValue(sve["status"])
                indiv = Individual(
                    name = sve["newConjointName"],
                    gender = sve["gender"],
                    dead = lv["dv"],
                    youngdead = lv["ydv"]
                )
                indiv.save()
                SVs.append(indiv.id)
            else:
                SVs.append(int(sve["conjointId"]))
        cmo.spouses.set(SVs)            
        cmo.save()
        # ######################

        return cmo.to_dict()

        









































# # LIST ALL ---------------------------------------
# @ns.route('/')
# class IndividualList(Resource):
#     @ns.doc('list_individuals')
#     @ns.marshal_list_with(individual_schema)
#     def get(self):
#         individuals = Individual.query.all()
#         return [individual.to_dict() for individual in individuals]

# # GET ONE ---------------------------------------
# @ns.route('/<int:id>')
# class IndividualDetails(Resource):
#     @ns.doc('get_individual')
#     @ns.marshal_with(individual_schema)
#     def get(self, id):
#         individual = Individual.query.get(id)
#         if individual:
#             return individual.to_dict()
#         return {"error": "Individual not found"}, 404

# # CREATE ---------------------------------------
# @ns.route('/add')
# class IndividualCreate(Resource):
#     @ns.doc('create_individual')
#     @ns.expect(individual_schema)
#     @ns.marshal_with(individual_schema, code=201)
#     def post(self):
#         data = api.payload
#         title = data['title']
#         description = data['description']
#         status = True

#         individual = Individual(title=title, description=description, status=status)
#         db.session.add(individual)
#         db.session.commit()

#         return individual.to_dict(), 201

# # UPDATE ---------------------------------------
# @ns.route('/update/<int:id>')
# class IndividualUpdate(Resource):
#     @ns.doc('update_individual')
#     @ns.expect(individual_schema)
#     @ns.marshal_with(individual_schema)
#     def put(self, id):
#         if not id or id != 0:
#             individual = Individual.query.get(id)
#             if individual:
#                 data = api.payload
#                 title = data['title']
#                 description = data['description']
#                 individual.title = title
#                 individual.description = description
#                 db.session.commit()
#                 return individual.to_dict()
#         return {"error": "Invalid ID"}, 400

# # DELETE ---------------------------------------
# @ns.route('/delete/<int:id>')
# class IndividualDelete(Resource):
#     @ns.doc('delete_individual')
#     @ns.response(204, 'Individual deleted')
#     def delete(self, id):
#         if not id or id != 0:
#             individual = Individual.query.get(id)
#             if individual:
#                 db.session.delete(individual)
#                 db.session.commit()
#                 return '', 204
#         return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
# @api.errorhandler(Exception)
# def handle_error(e):
#     return {"message": "An unexpected error occurred: " + str(e)}, 500
