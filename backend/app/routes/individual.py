from flask import Blueprint, request, redirect, jsonify, render_template, send_from_directory
# from flask import Flaskfrom flask import send_from_directory
from flask_restx import Resource, Api, fields, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app import api, app
from app.models import db
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool
from app.models.individual import Individual
from app.schemas.individual import ns, individual_schema, individual_fields, \
      all_individuals_response, individual_response, individual_form_data_response
import json, os, time, random
from PIL import Image
from datetime import datetime, date

date_format = "%Y-%m-%d"

# upload_parser = reqparse.RequestParser()
# # upload_parser.add_argument('file', location='files', type=FileStorage, required=True)
# upload_parser.add_argument('title', type=str, required=True, location='form', help='Title is required')
# upload_parser.add_argument('description', type=str, required=True, location='form', help='Description is required')
# upload_parser.add_argument('picture', type=FileStorage, required=True, location='files', help='Picture is required')

document_root = app.config['UPLOAD_FOLDER']
photos_root = app.config['UPLOAD_FOLDER']+'/photos'


# @api.route('/upload')
# class UploadFile(Resource):
#     @ns.doc('upload_post')
#     @api.expect(upload_parser)
#     def post(self):
#         # args = upload_parser.parse_args()
#         # file = args['file']
#         args = upload_parser.parse_args()
#         title = args['title']
#         description = args['description']
#         picture = args['picture']
#         if picture:
#             filename = secure_filename(picture.filename)
#             picture.save(os.path.join(document_root, filename))
#             return {'message': 'File uploaded successfully', 'filename': filename}, 201

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(document_root, filename)



# FORM DATA ---------------------------------------
@ns.route('/form_data/<int:id>')
class IndividualFormData(Resource):
    @ns.doc('individual_form_data')
    @ns.marshal_with(individual_form_data_response)
    def get(self, id):
        ALL = {
            "all":[],
            "alive": [],
            "dead": [],
            "youngdead": [],
        }
        MALES = {
            "all":[],
            "alive": [],
            "dead": [],
            "youngdead": [],
        }
        FEMALES = {
            "all":[],
            "alive": [],
            "dead": [],
            "youngdead": [],
        }

        for indiv in Individual.query.all():
            idv =  {"id": indiv.id, "name": indiv.name}
            ALL["all"].append(idv)

            if indiv.gender == 'm':
                MALES["all"].append(idv)
                if indiv.dead == False:
                    ALL["alive"].append(idv)                
                    MALES["alive"].append(idv)
                elif indiv.dead == True:
                    if indiv.youngdead == False:
                        ALL["dead"].append(idv)
                        MALES["dead"].append(idv)
                    elif indiv.youngdead == True:
                        ALL["youngdead"].append(idv)
                        MALES["youngdead"].append(idv)

            elif indiv.gender == 'f':
                FEMALES["all"].append(idv)
                if indiv.dead == False:
                    ALL["alive"].append(idv)                
                    FEMALES["alive"].append(idv)
                elif indiv.dead == True:
                    if indiv.youngdead == False:
                        ALL["dead"].append(idv)
                        FEMALES["dead"].append(idv)
                    elif indiv.youngdead == True:
                        ALL["youngdead"].append(idv)
                        FEMALES["youngdead"].append(idv)



        # ###########
        cm = {}
        if not id or id != 0:
            cmo = Individual.query.get(id)
            # #####################
            cmoFather = None
            cmoMother = None
            if cmo.parent_male_id :
                cmoFather = Individual.query.get(cmo.parent_male_id)
            if cmo.parent_female_id :
                cmoMother = Individual.query.get(cmo.parent_female_id)
            # ############################
            cmoSpouses = []
            for cmosp in cmo.spouses:
                spouseObject = cmosp
                spouse = {
                    "id":spouseObject.id,
                    "name": spouseObject.name,
                    "gender": spouseObject.gender,
                    "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead),
                }
                cmoSpouses.append(spouse)

            cm = {
                "myPhoto": cmo.photoPath,
                "myPhotoName": cmo.photoName,
                "myName": cmo.name,
                "myGender": cmo.gender,
                "myLifeStatus": lifeStatusFrontend(cmo.dead, cmo.youngdead),
                "father": {
                    "id": None if cmoFather == None else cmoFather.id,
                    "name": None if cmoFather == None else cmoFather.name,
                    "gender": None if cmoFather == None else cmoFather.gender,
                    "status": None if cmoFather == None else lifeStatusFrontend(cmoFather.dead, cmoFather.youngdead),
                },
                "mother": {
                    "id": None if cmoMother == None else cmoMother.id,
                    "name": None if cmoMother == None else cmoMother.name,
                    "gender": None if cmoMother == None else cmoMother.gender,
                    "status": None if cmoMother == None else lifeStatusFrontend(cmoMother.dead, cmoMother.youngdead),
                },
                
                "spouses": cmoSpouses,
                "birthrank": cmo.birth_rank,
                "birthdate": cmo.birth_date,
                "birthplace": cmo.birth_place,
                "email": cmo.email,
                "telephone": cmo.telephone,
                "profession": cmo.profession,
                "country": cmo.country,
                "city": cmo.city,
                "linkedin": cmo.linkedin,
                "twitter": cmo.twitter,
                "facebook": cmo.facebook,
                "instagram": cmo.instagram,
                "aboutme": cmo.aboutme,
                "isIncomingSpouse": cmo.isIncomingSpouse,
                "sFatherName": cmo.sFatherName,
                "sFatherStatus": lifeStatusFrontend(cmo.sFatherDead, False),
                "sMotherName": cmo.sMotherName,
                "sMotherStatus": lifeStatusFrontend(cmo.sMotherDead, False),
            }

            response = {
                "allMembers":ALL, 
                "allMales":MALES, 
                "allFemales": FEMALES,
                "currentMember": cm,
            }

            return response
    

# LIST ALL ---------------------------------------
@ns.route('/list')
class IndividualList(Resource):
    @ns.doc('all_individuals')
    @ns.marshal_with(all_individuals_response)
    # @ns.response(200, 'Success', all_individuals_response)
    # @ns.produces('application/json')
    def get(self):
        FAMILY = []
        FAMILY_GENERATIONS = []
        GENERATION_0 = []
        for indiv in Individual.query.all(): 

            # print("/////////////////////////////////////////////////////////")
            # print(indiv.spouses)
            # print("/////////////////////////////////////////////////////////")
            indiv_spouses = []
            if is_iterable(indiv.spouses):
                for sp in indiv.spouses:
                    indiv_spouses.append(sp.id)
                    
            indivItem = {
                "id": indiv.id,
                "name": indiv.name,
                "gender": indiv.gender,
                "alive": not indiv.dead,
                "father": indiv.parent_male_id,
                "mother": indiv.parent_female_id,
                "spouses": indiv_spouses,
                "generation": None,
                "dead": indiv.dead,
                "photo": indiv.photoPath if indiv.photoName else None,
                "isIncomingSpouse": indiv.isIncomingSpouse,
            }
            # If Indiv has no parent and his/her spouse has no parent too then he's Generation 0
            if not indiv.parent_male_id and not indiv.parent_female_id:
                sp_flag = False
                if len(indiv_spouses)  > 0 :                    
                    for isp in indiv_spouses:
                        isp_obj = Individual.query.get(isp)
                        if isp_obj.parent_male_id or isp_obj.parent_female_id:
                            # flag=True if Indiv spouse has a parent => then Indiv is not of Generation 0
                            sp_flag = True

                # flag=False => Indiv spouse has no parent => then Indiv is of Generation 0
                if not sp_flag:
                    indivItem["generation"] = 0
                    GENERATION_0.append(indiv.id)

            # print("income list loop ongoing !!")
            FAMILY.append(indivItem)

        # Remove duplicates
        GENERATION_0 = list(dict.fromkeys(GENERATION_0))
        FAMILY_GENERATIONS.append(GENERATION_0)

        # family_generations = []
        FAMILY_GENERATIONS, nb_gen, largest_gen = process_generations(FAMILY, FAMILY_GENERATIONS)

        response = {
            "family": FAMILY,
            "familyGenerations": FAMILY_GENERATIONS,
            "largest_gen": largest_gen,
            "nb_gen": nb_gen,
            "len_family": len(FAMILY),
        }

        return response

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class IndividualDetails(Resource):
    @ns.doc('get_individual')
    @ns.marshal_with(individual_response)
    def get(self, id):
        cmo = Individual.query.get(id)
        if cmo:
            # #####################
            cmoFather = None
            cmoMother = None
            if cmo.parent_male_id :
                cmoFather = Individual.query.get(cmo.parent_male_id)
            if cmo.parent_female_id :
                cmoMother = Individual.query.get(cmo.parent_female_id)
            # ############################
            cmoSpouses = []
            if is_iterable(cmo.spouses):
                for cmosp in cmo.spouses:
                    spouseObject = cmosp 
                    spouse = {
                        "id":spouseObject.id,
                        "name": spouseObject.name,
                        "gender": genderFrontend(spouseObject.gender),
                        "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead, spouseObject.gender),
                    }
                    cmoSpouses.append(spouse)

            cm = {
                "myPhoto": cmo.photoPath,
                "myPhotoName": cmo.photoName,
                "myID": cmo.id,
                "myName": cmo.name,
                "myInitials": getFirst2Initials(cmo.name),
                "myGender": genderFrontend(cmo.gender),
                "myLifeStatus": lifeStatusFrontend(cmo.dead, cmo.youngdead, cmo.gender),
                "father": {
                    "id": None if cmoFather == None else cmoFather.id,
                    "name": None if cmoFather == None else cmoFather.name,
                    "gender": None if cmoFather == None else genderFrontend(cmoFather.gender),
                    "status": None if cmoFather == None else lifeStatusFrontend(cmoFather.dead, cmoFather.youngdead, cmoFather.gender),
                },
                "mother": {
                    "id": None if cmoMother == None else cmoMother.id,
                    "name": None if cmoMother == None else cmoMother.name,
                    "gender": None if cmoMother == None else genderFrontend(cmoMother.gender),
                    "status": None if cmoMother == None else lifeStatusFrontend(cmoMother.dead, cmoMother.youngdead, cmoMother.gender),
                },
                
                "spouses": cmoSpouses,
                "len_spouses": len(cmoSpouses),
                "birthrank": '' if cmo.birth_rank == None else cmo.birth_rank,
                "birthdate": '' if cmo.birth_date == None else cmo.birth_date,
                "birthplace": '' if cmo.birth_place == None else cmo.birth_place,
                "email": '' if cmo.email == None else cmo.email,
                "telephone": '' if cmo.telephone == None else cmo.telephone,
                "profession": '' if cmo.profession == None else cmo.profession,
                "country": '' if cmo.country == None else cmo.country,
                "city": '' if cmo.city == None else cmo.city,
                "linkedin": '' if cmo.linkedin == None else cmo.linkedin,
                "twitter": '' if cmo.twitter == None else cmo.twitter,
                "facebook": '' if cmo.facebook == None else cmo.facebook,
                "instagram": '' if cmo.instagram == None else cmo.instagram,
                "aboutme": '' if cmo.aboutme == None else cmo.aboutme,
            }

            if cmo.isIncomingSpouse :
                cm["father"]["id"] = random.randint(300, 700)
                cm["father"]["name"] = cmo.sFatherName
                cm["father"]["status"] = lifeStatusFrontend(cmo.sFatherDead, False, 'm')
                cm["mother"]["id"] = random.randint(300, 700)
                cm["mother"]["name"] = cmo.sMotherName
                cm["mother"]["status"] = lifeStatusFrontend(cmo.sMotherDead, False, 'f')
            
            return cm
        
        return {"error": "Individual not found"}, 404


# CREATE ---------------------------------------
@ns.route('/add')
class NewFamilyMember(Resource):
    @ns.doc('new_individual')
    @api.expect(individual_schema)
    @ns.marshal_with(individual_fields, code=201)
    @ns.response(200, 'Success', individual_response)
    def post(self):
        args = individual_schema.parse_args()
        
        def get_arg(key):
            return args[key]

        my_lv = lifeValue(get_arg('myLifeStatus'))

        fatherId = process_parents(str_to_bool(get_arg('hasFatherCheck')), str_to_bool(get_arg('newFatherCheck')), str_to_bool(get_arg('urlLastButOneItem')), get_arg('fatherId'), get_arg('newFatherName'), get_arg('fatherLifeStatusValue'), 'm')
        motherId = process_parents(str_to_bool(get_arg('hasMotherCheck')), str_to_bool(get_arg('newMotherCheck')), str_to_bool(get_arg('urlLastButOneItem')), get_arg('motherId'), get_arg('newMotherName'), get_arg('motherLifeStatusValue'), 'f')      


        cmo = Individual(
            name = get_arg('myName'),
            gender = get_arg('myGender'),
            dead = my_lv["dv"],
            youngdead = my_lv["ydv"],
            generation = None,
            parent_male_id = fatherId,
            parent_female_id = motherId,
            birth_rank = get_arg('birthrank'),
            birth_date = datetime.strptime(get_arg('birthdate'), date_format) if is_valid_date(get_arg('birthdate')) else date.today(),
            birth_place = get_arg('birthplace'),
            email = get_arg('email'),
            telephone = get_arg('telephone'),
            profession = get_arg('profession'),
            country = get_arg('country'),
            city = get_arg('city'),
            linkedin = get_arg('linkedin'),
            twitter = get_arg('twitter'),
            facebook = get_arg('facebook'),
            instagram = get_arg('instagram'),
            aboutme = get_arg('aboutme'),
            isIncomingSpouse = str_to_bool(get_arg('isIncomingSpouse')),
        )
        
        if get_arg('urlLastButOneItem') == 'new_spouse':
            cmo.isIncomingSpouse = True
            cmo.sFatherName, cmo.sMotherName = get_arg('newFatherName'), get_arg('newMotherName')
            flv, mlv = lifeValue(get_arg('fatherLifeStatusValue')), lifeValue(get_arg('motherLifeStatusValue'))
            cmo.sFatherDead, cmo.sMotherDead = flv["dv"], mlv["dv"]
        
        if str_to_bool(get_arg('noPhotoCheck')):
            cmo.photoName, cmo.photoPath = None, None
        else:
            if not(get_arg('noPhotoCheck')) and get_arg('uploadedPhotoName'):
                # Save the new file
                timestr = time.strftime("%Y%m%d-%H%M%S")
                photoName = 'Photo-'+timestr+".jpg"                
                pathToConvertedFiles = os.path.join(photos_root, 'photos', photoName)
                relativePathToConvertedFiles = os.path.join('photos', photoName)
                img = Image.open(get_arg('uploadedPhoto'))
                img = img.convert('RGB')
                img.thumbnail((256, 256))
                img.save(pathToConvertedFiles)                
                cmo.photoName, cmo.photoPath = photoName, pathToConvertedFiles

        # cmo.save()
        if get_arg('spouseValues'):
            SVs = []
            for sve in json.loads(get_arg('spouseValues')):
                if str_to_bool(sve["newConjointCheck"]):
                    lv = lifeValue(sve["status"])
                    indiv = Individual(name=sve["newConjointName"], gender=sve["gender"], dead=lv["dv"], youngdead=lv["ydv"])
                    indiv.save()
                    SVs.append(indiv.id)
                else:
                    spouse = Individual.query.get(int(sve["conjointId"]))
                    SVs.append(spouse)
                    # SVs.append(int(sve["conjointId"]))

            cmo.set_spouses(SVs)             
        cmo.save()

        return cmo.to_dict()


# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class IndividualUpdate(Resource):
    @ns.doc('update_individual')
    @api.expect(individual_schema)
    # @ns.marshal_with(individual_schema)
    def put(self, id):
        if not id or id != 0:
            args = individual_schema.parse_args()
            
            def get_arg(key):
                return args[key]

            my_lv = lifeValue(get_arg('myLifeStatus'))
            fatherId = process_parents(str_to_bool(get_arg('hasFatherCheck')), str_to_bool(get_arg('newFatherCheck')), str_to_bool(get_arg('urlLastButOneItem')), get_arg('fatherId'), get_arg('newFatherName'), get_arg('fatherLifeStatusValue'), 'm')
            motherId = process_parents(str_to_bool(get_arg('hasMotherCheck')), str_to_bool(get_arg('newMotherCheck')), str_to_bool(get_arg('urlLastButOneItem')), get_arg('motherId'), get_arg('newMotherName'), get_arg('motherLifeStatusValue'), 'f')      
            
            cmo = Individual.query.get(id)
            cmo.name, cmo.gender, cmo.dead, cmo.youngdead = get_arg('myName'), get_arg('myGender'), my_lv["dv"], my_lv["ydv"]
            cmo.generation, cmo.parent_male_id, cmo.parent_female_id = None, fatherId, motherId
            
            cmo.birth_rank, cmo.birth_date, cmo.birth_place = None if get_arg('birthrank') == '' else get_arg('birthrank'), \
                datetime.strptime(get_arg('birthdate'), date_format) if is_valid_date(get_arg('birthdate')) else date.today(), \
                    get_arg('birthplace')
            cmo.email, cmo.telephone, cmo.profession, cmo.country, cmo.city = get_arg('email'), get_arg('telephone'), get_arg('profession'), get_arg('country'), get_arg('city')
            cmo.linkedin, cmo.twitter, cmo.facebook, cmo.instagram, cmo.aboutme = get_arg('linkedin'), get_arg('twitter'), get_arg('facebook'), get_arg('instagram'), get_arg('aboutme')
            cmo.isIncomingSpouse = str_to_bool(get_arg('isIncomingSpouse'))

            if str_to_bool(get_arg('isIncomingSpouse')):
                cmo.sFatherName, cmo.sMotherName = get_arg('newFatherName'), get_arg('newMotherName')
                flv, mlv = lifeValue(get_arg('fatherLifeStatusValue')), lifeValue(get_arg('motherLifeStatusValue'))
                cmo.sFatherDead, cmo.sMotherDead = flv["dv"], mlv["dv"]
            
            # print("/////////////////////////////////////////////////////////")
            # print(str_to_bool(get_arg('noPhotoCheck')))
            # print("*********************************************************")
            # print(get_arg('uploadedPhoto'))
            # print("/////////////////////////////////////////////////////////")

            if str_to_bool(get_arg('noPhotoCheck')):
                cmo.photoName, cmo.photoPath = None, None
                # Delete the old file if it exists
                old_filename = get_arg('old_filename')
                if old_filename and os.path.exists(os.path.join(photos_root, old_filename)):
                    os.remove(os.path.join(photos_root, old_filename))
            else:
                if get_arg('uploadedPhoto'):
                    # Delete the old file if it exists
                    old_filename = get_arg('old_filename')
                    if old_filename and os.path.exists(os.path.join(photos_root, old_filename)):
                        os.remove(os.path.join(photos_root, old_filename))

                    # Save the new file
                    # filename = secure_filename(get_arg('uploadedPhoto').filename)
                    # get_arg('uploadedPhoto').save(os.path.join(photos_root, filename))
                    # cmo.photoName, cmo.photoPath = filename, os.path.join(photos_root, filename)
                    timestr = time.strftime("%Y%m%d-%H%M%S")
                    photoName = 'Photo-'+timestr+".jpg"                
                    pathToConvertedFiles = os.path.join(photos_root, photoName)
                    relativePathToConvertedFiles = os.path.join('photos', photoName)
                    img = Image.open(get_arg('uploadedPhoto'))
                    img = img.convert('RGB')
                    img.thumbnail((256, 256))
                    img.save(pathToConvertedFiles)                
                    cmo.photoName, cmo.photoPath = photoName, pathToConvertedFiles
            
            # cmo.save()
            if get_arg('spouseValues'):
                SVs = []
                for sve in json.loads(get_arg('spouseValues')):
                    if str_to_bool(sve["newConjointCheck"]):
                        lv = lifeValue(sve["status"])
                        indiv = Individual(name=sve["newConjointName"], gender=sve["gender"], dead=lv["dv"], youngdead=lv["ydv"])
                        indiv.save()
                        SVs.append(indiv.id)
                    else:
                        spouse = Individual.query.get(int(sve["conjointId"]))
                        SVs.append(spouse)
                        # SVs.append(int(sve["conjointId"]))
                
                cmo.set_spouses(SVs)            
            cmo.save()

            return cmo.to_dict()
        
        return {"error": "Invalid ID"}, 400

        
# # DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class IndividualDelete(Resource):
    @ns.doc('delete_individual')
    @ns.response(204, 'Individual deleted')
    def delete(self, id):
        if not id or id != 0:
            individual = Individual.query.get(id)
            if individual:
                individual.delete()                
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500








































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
