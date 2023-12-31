from flask import Blueprint, request, redirect, jsonify, render_template, send_from_directory
# from flask import Flaskfrom flask import send_from_directory
from flask_restx import Resource, Api, fields, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from app import api, app
from app.models import db
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids
from app.models.family import Family
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
            if is_iterable(cmo.spouses):
                for cmosp in cmo.spouses:
                    spouseObject = cmosp
                    spouse = {
                        "id":spouseObject.id,
                        "name": spouseObject.name,
                        "gender": spouseObject.gender,
                        "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead),
                    }
                    cmoSpouses.append(spouse)
            
            # ############################
            cmoFamilies = []
            if is_iterable(cmo.families):
                for cmosp in cmo.families:
                    familyObject = cmosp 
                    family = {
                        "id":familyObject.id,
                        "name": familyObject.name,                        
                    }
                    cmoFamilies.append(family)

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
                "families": cmoFamilies,
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
                "is_ghost": cmo.is_ghost,
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

            indivFather = None
            indivMother = None
            if indiv.parent_male_id :
                indivFather = Individual.query.get(indiv.parent_male_id)
            if indiv.parent_female_id :
                indivMother = Individual.query.get(indiv.parent_female_id)
            
            # ############################
            indivChildren = []
            myChildren1 = Individual.query.filter_by(parent_male_id=indiv.id).all()
            myChildren2 = Individual.query.filter_by(parent_female_id=indiv.id).all()
            unique_children = list(set(myChildren1) | set(myChildren2))
            for indivChild in unique_children:
                childObject = indivChild 
                child = {
                    "id": int(childObject.id),
                    "name": childObject.name,
                    "gender": genderFrontend(childObject.gender),
                    "status": lifeStatusFrontend(childObject.dead, childObject.youngdead, childObject.gender),
                }
                indivChildren.append(child)

            # ############################
            indivSpouses = []
            if is_iterable(indiv.spouses):
                for indivsp in indiv.spouses:
                    spouseObject = indivsp 
                    spouse = {
                        "id": int(spouseObject.id),
                        "name": spouseObject.name,
                        "gender": genderFrontend(spouseObject.gender),
                        "status": lifeStatusFrontend(spouseObject.dead, spouseObject.youngdead, spouseObject.gender),
                    }
                    indivSpouses.append(spouse)
            
            # ############################
            indivFamilies = []
            if is_iterable(indiv.families):
                for indivsp in indiv.families:
                    familyObject = indivsp 
                    family = {
                        "id":familyObject.id,
                        "name": familyObject.name,
                    }
                    indivFamilies.append(family)

            indivItem = {
                "id": indiv.id,
                "generation": None,
                "myPhoto": indiv.photoPath,
                "myPhotoName": indiv.photoName,
                "myID": indiv.id,
                "myName": indiv.name,                
                "myInitials": getFirst2Initials(indiv.name),
                "myGender": genderFrontend(indiv.gender),
                "myLifeStatus": lifeStatusFrontend(indiv.dead, indiv.youngdead, indiv.gender),
                "father": {
                    "id": None if indivFather == None else int(indivFather.id),
                    "name": None if indivFather == None else indivFather.name,
                    "gender": None if indivFather == None else genderFrontend(indivFather.gender),
                    "status": None if indivFather == None else lifeStatusFrontend(indivFather.dead, indivFather.youngdead, indivFather.gender),
                },
                "mother": {
                    "id": None if indivMother == None else int(indivMother.id),
                    "name": None if indivMother == None else indivMother.name,
                    "gender": None if indivMother == None else genderFrontend(indivMother.gender),
                    "status": None if indivMother == None else lifeStatusFrontend(indivMother.dead, indivMother.youngdead, indivMother.gender),
                },
                
                "spouses": indivSpouses,
                "children":indivChildren,
                "families": indivFamilies,                
                "len_spouses": len(indivSpouses),
                "birthrank": '' if indiv.birth_rank == None else indiv.birth_rank,
                "birthdate": '' if indiv.birth_date == None else indiv.birth_date,
                "birthplace": '' if indiv.birth_place == None else indiv.birth_place,
                "email": '' if indiv.email == None else indiv.email,
                "telephone": '' if indiv.telephone == None else indiv.telephone,
                "profession": '' if indiv.profession == None else indiv.profession,
                "country": '' if indiv.country == None else indiv.country,
                "city": '' if indiv.city == None else indiv.city,
                "linkedin": '' if indiv.linkedin == None else indiv.linkedin,
                "twitter": '' if indiv.twitter == None else indiv.twitter,
                "facebook": '' if indiv.facebook == None else indiv.facebook,
                "instagram": '' if indiv.instagram == None else indiv.instagram,
                "aboutme": '' if indiv.aboutme == None else indiv.aboutme,
                "is_ghost": indiv.is_ghost,
                
            }

            if indiv.isIncomingSpouse :
                indivItem["father"]["id"] = random.randint(300, 700)
                indivItem["father"]["name"] = indiv.sFatherName
                indivItem["father"]["status"] = lifeStatusFrontend(indiv.sFatherDead, False, 'm')
                indivItem["mother"]["id"] = random.randint(300, 700)
                indivItem["mother"]["name"] = indiv.sMotherName
                indivItem["mother"]["status"] = lifeStatusFrontend(indiv.sMotherDead, False, 'f') 

            # print("/////////////////////////////////////////////////////////")
            # print(indiv.spouses)
            # print("/////////////////////////////////////////////////////////")
            # indiv_spouses = []
            # if is_iterable(indiv.spouses):
            #     for sp in indiv.spouses:
            #         indiv_spouses.append(sp.id)
                    
            # indivItem = {
            #     "id": indiv.id,
            #     "name": indiv.name,
            #     "gender": indiv.gender,
            #     "alive": not indiv.dead,
            #     "father": indiv.parent_male_id,
            #     "mother": indiv.parent_female_id,
            #     "spouses": indiv_spouses,
            #     "generation": None,
            #     "dead": indiv.dead,
            #     "photo": indiv.photoPath if indiv.photoName else None,
            #     "isIncomingSpouse": indiv.isIncomingSpouse,
            #     "is_ghost": indiv.is_ghost,
            # }
            # If Indiv has no parent and his/her spouse has no parent too then he's Generation 0
            if not indiv.parent_male_id and not indiv.parent_female_id:
                sp_flag = False
                if len(indivSpouses)  > 0 :
                    for isp in indivSpouses:
                        isp_obj = Individual.query.get(isp["id"])
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
            indivChildren = []
            myChildren1 = Individual.query.filter_by(parent_male_id=cmo.id).all()
            myChildren2 = Individual.query.filter_by(parent_female_id=cmo.id).all()
            unique_children = list(set(myChildren1) | set(myChildren2))
            for indivChild in unique_children:
                childObject = indivChild 
                child = {
                    "id": int(childObject.id),
                    "name": childObject.name,
                    "gender": genderFrontend(childObject.gender),
                    "status": lifeStatusFrontend(childObject.dead, childObject.youngdead, childObject.gender),
                }
                indivChildren.append(child)

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
            
            # ############################
            cmoFamilies = []
            if is_iterable(cmo.families):
                for cmosp in cmo.families:
                    familyObject = cmosp 
                    family = {
                        "id":familyObject.id,
                        "name": familyObject.name,
                    }
                    cmoFamilies.append(family)

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
                "children": indivChildren,
                "families": cmoFamilies,
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
                "is_ghost": cmo.is_ghost,
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
            username = get_arg('myUsername'),            
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
            is_ghost = str_to_bool(get_arg('is_ghost')),
            is_deleted = str_to_bool(get_arg('is_deleted'))
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
                spouse = Individual.query.get(int(sve))
                SVs.append(spouse)
                # if str_to_bool(sve["newConjointCheck"]):
                #     lv = lifeValue(sve["status"])
                #     indiv = Individual(name=sve["newConjointName"], gender=sve["gender"], dead=lv["dv"], youngdead=lv["ydv"])
                #     indiv.save()
                #     SVs.append(indiv.id)
                # else:
                #     spouse = Individual.query.get(int(sve["conjointId"]))
                #     SVs.append(spouse)

            cmo.set_spouses(SVs)

        if get_arg('families'):
            # individual_families_ids = get_ids(cmo.families)
            # individual_families = cmo.families
            individual_families = []
            for fmlyID in json.loads(get_arg('families')):
                fmly = Family.query.get(int(fmlyID))
                individual_families.append(fmly)

            cmo.set_families(individual_families)

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
            cmo.username, cmo.is_ghost, cmo.is_deleted = get_arg('myUsername'), str_to_bool(get_arg('is_ghost')), str_to_bool(get_arg('is_deleted'))
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
                    spouse = Individual.query.get(int(sve))
                    SVs.append(spouse)
                    # if str_to_bool(sve["newConjointCheck"]):
                    #     lv = lifeValue(sve["status"])
                    #     indiv = Individual(name=sve["newConjointName"], gender=sve["gender"], dead=lv["dv"], youngdead=lv["ydv"])
                    #     indiv.save()
                    #     SVs.append(indiv.id)
                    # else:
                    #     spouse = Individual.query.get(int(sve["conjointId"]))
                    #     SVs.append(spouse)
                
                cmo.set_spouses(SVs)

            if get_arg('families'):
                # individual_families_ids = get_ids(cmo.families)
                # individual_families = cmo.families
                individual_families = []
                for fmlyID in json.loads(get_arg('families')):
                    fmly = Family.query.get(int(fmlyID))
                    individual_families.append(fmly)

                cmo.set_families(individual_families)
                            
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
