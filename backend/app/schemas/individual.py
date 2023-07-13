
from flask_restx import Resource, Api, fields, reqparse
from app import api
from werkzeug.datastructures import FileStorage

ns = api.namespace('individuals', description='Individual operations')

individual_schema = reqparse.RequestParser()

individual_schema.add_argument('currentMemberId', type=int, required=False, location='form', help='')
individual_schema.add_argument('urlLastButOneItem', type=str, required=False, location='form', help='')
individual_schema.add_argument('myName', type=str, required=True, location='form', help='This is required')
individual_schema.add_argument('myGender', type=str, required=True, location='form', help='This is required')
individual_schema.add_argument('myLifeStatus', type=str, required=False, location='form', help='')
individual_schema.add_argument('isIncomingSpouse', type=str, required=True, default=False, location='form', help='This is required')
individual_schema.add_argument('noPhotoCheck', type=str, required=False, default=False, location='form', help='')
individual_schema.add_argument('old_filename', type=str, required=False, location='form', help='')
individual_schema.add_argument('uploadedPhotoName', type=str, required=False, location='form', help='')

individual_schema.add_argument('uploadedPhoto', type=FileStorage, required=False, location='files', help='uploadedPhoto is required')

individual_schema.add_argument('fatherId', type=int, required=False, location='form', help='')
individual_schema.add_argument('newFatherCheck', type=str, required=False, default=False, location='form', help='')
individual_schema.add_argument('newFatherName', type=str, required=False, location='form', help='')
individual_schema.add_argument('hasFatherCheck', type=str, required=False, default=False, location='form', help='')
individual_schema.add_argument('fatherLifeStatusValue', type=str, required=False, location='form', help='')
individual_schema.add_argument('motherId', type=int, required=False, location='form', help='')
individual_schema.add_argument('newMotherCheck', type=str, required=False, default=False, location='form', help='')
individual_schema.add_argument('newMotherName', type=str, required=False, location='form', help='')
individual_schema.add_argument('hasMotherCheck', type=str, required=False, default=False, location='form', help='')
individual_schema.add_argument('motherLifeStatusValue', type=str, required=False, location='form', help='')

individual_schema.add_argument('spouseValues', type=str, required=False, location='form', help='')

individual_schema.add_argument('birthdate', type=str, required=False, location='form', help='')
individual_schema.add_argument('birthplace', type=str, required=False, location='form', help='')
individual_schema.add_argument('birthrank', type=str, required=False, location='form', help='')
individual_schema.add_argument('email', type=str, required=False, location='form', help='')
individual_schema.add_argument('telephone', type=str, required=False, location='form', help='')
individual_schema.add_argument('profession', type=str, required=False, location='form', help='')
individual_schema.add_argument('country', type=str, required=False, location='form', help='')
individual_schema.add_argument('city', type=str, required=False, location='form', help='')
individual_schema.add_argument('linkedin', type=str, required=False, location='form', help='')
individual_schema.add_argument('twitter', type=str, required=False, location='form', help='')
individual_schema.add_argument('facebook', type=str, required=False, location='form', help='')
individual_schema.add_argument('instagram', type=str, required=False, location='form', help='')
individual_schema.add_argument('aboutme', type=str, required=False, location='form', help='')



individual_fields = ns.model('IndividualFields', {
    'currentMemberId': fields.Integer,
    'urlLastButOneItem': fields.String,
    'myName': fields.String,
    'myGender': fields.String,
    'myLifeStatus': fields.String,
    'isIncomingSpouse': fields.String,
    'noPhotoCheck': fields.String,
    'uploadedPhotoName': fields.String,
    'uploadedPhoto': fields.Raw(required=False, description='Individual uploadPhoto', type='file'),
    'fatherId': fields.Integer,
    'newFatherCheck': fields.String,
    'newFatherName': fields.String,
    'hasFatherCheck': fields.String,
    'fatherLifeStatusValue': fields.String,
    'motherId': fields.Integer,
    'newMotherCheck': fields.String,
    'newMotherName': fields.String,
    'hasMotherCheck': fields.String,
    'motherLifeStatusValue': fields.String,
    'spouseValues': fields.String,
    'birthdate': fields.String,
    'birthplace': fields.String,
    'birthrank': fields.String,
    'email': fields.String,
    'telephone': fields.String,
    'profession': fields.String,
    'country': fields.String,
    'city': fields.String,
    'linkedin': fields.String,
    'twitter': fields.String,
    'facebook': fields.String,
    'instagram': fields.String,
    'aboutme': fields.String,
})








individual_model = ns.model('IndividualModel', {
    "id": fields.Integer,
    "name": fields.String,
    "gender": fields.String,
    "alive": fields.Boolean,
    "father": fields.Integer,
    "mother": fields.Integer,
    "spouses": fields.List(fields.Integer),
    "generation": fields.Integer,
    "dead": fields.Boolean,
    "photo": fields.String,
    "isIncomingSpouse": fields.Boolean,
})
largest_gen_model = ns.model('IndividualModel', {
    "rank": fields.Integer,
    "size": fields.Integer,
})
all_individuals_response = ns.model('ResponseModel', {
    'family': fields.List(fields.Nested(individual_model)),
    'familyGenerations': fields.List(fields.List(fields.Integer)),
    'largest_gen': fields.Nested(largest_gen_model),
    'nb_gen': fields.Integer,
    'len_family': fields.Integer
})



parent_fields = ns.model('Parent', {
    'id': fields.Integer,
    'name': fields.String,
    'gender': fields.String,
    'status': fields.String
})

spouse_fields = ns.model('Spouse', {
    'id': fields.Integer,
    'name': fields.String,
    'gender': fields.String,
    'status': fields.String
})

individual_response = ns.model('Individual', {
    'myPhoto': fields.String,
    "myPhotoName": fields.String,
    'myID': fields.Integer,
    'myName': fields.String,
    'myInitials': fields.String,
    'myGender': fields.String,
    'myLifeStatus': fields.String,
    'father': fields.Nested(parent_fields),
    'mother': fields.Nested(parent_fields),
    'spouses': fields.List(fields.Nested(spouse_fields)),
    'len_spouses': fields.Integer,
    'birthrank': fields.String,
    'birthdate': fields.String,
    'birthplace': fields.String,
    'email': fields.String,
    'telephone': fields.String,
    'profession': fields.String,
    'country': fields.String,
    'city': fields.String,
    'linkedin': fields.String,
    'twitter': fields.String,
    'facebook': fields.String,
    'instagram': fields.String,
    'aboutme': fields.String
})

# =======================================================================================

member_model = api.model('MemberModel', {
    "id": fields.Integer,
    "name": fields.String,
})
individu_status_model = api.model('IndividuStatusModel', {
    "all": fields.List(fields.Nested(member_model)),
    "alive": fields.List(fields.Nested(member_model)),
    "dead": fields.List(fields.Nested(member_model)),
    "youngdead": fields.List(fields.Nested(member_model)),
})
spouse_model = api.model('SpouseModel', {
    "id": fields.Integer,
    "name": fields.String,
    "gender": fields.String,
    "status": fields.String,
})
parent_model = api.model('ParentModel', {
    "id": fields.Integer,
    "name": fields.String,
    "gender": fields.String,
    "status": fields.String,
})
current_member_model = api.model('CurrentMemberModel', {
    "myPhoto": fields.String,
    "myPhotoName": fields.String,
    "myName": fields.String,
    "myGender": fields.String,
    "myLifeStatus": fields.String,
    "father": fields.Nested(parent_model),
    "mother": fields.Nested(parent_model),
    "spouses": fields.List(fields.Nested(spouse_model)),
    "birthrank": fields.Integer,
    "birthdate": fields.String,
    "birthplace": fields.String,
    "email": fields.String,
    "telephone": fields.String,
    "profession": fields.String,
    "country": fields.String,
    "city": fields.String,
    "linkedin": fields.String,
    "twitter": fields.String,
    "facebook": fields.String,
    "instagram": fields.String,
    "aboutme": fields.String,
    "isIncomingSpouse": fields.Boolean,
    "sFatherName": fields.String,
    "sFatherStatus": fields.String,
    "sMotherName": fields.String,
    "sMotherStatus": fields.String,
})
individual_form_data_response = api.model('ResponseModel', {
    "allMembers": fields.Nested(individu_status_model),
    "allMales": fields.Nested(individu_status_model),
    "allFemales": fields.Nested(individu_status_model),
    "currentMember": fields.Nested(current_member_model),
})


# indivItem = {
#                 "id": indiv.id,
#                 "name": indiv.name,
#                 "gender": indiv.gender,
#                 "alive": not indiv.dead,
#                 "father": indiv.parent_male_id,
#                 "mother": indiv.parent_female_id,
#                 "spouses": indiv_spouses,
#                 "generation": None
#             }
# oneConj= {
#     "index": nbConjoints,
#     "gender": null,
#     "status": null,
#     "conjointId":null,
#     "conjointRank":null,
#     "newConjointCheck":false,
#     "newConjointName": null
# }


# individual_schema = api.model('Individual', {
#     'id' : fields.Integer(required=True,description='Individual id'),
#     'name' : fields.String(required=True,description='Individual name'),
#     'gender' : fields.String(required=True,description='Individual gender'),
#     'generation' : fields.Integer(required=True,description='Individual generation'),
#     'parent_male_id' : fields.Integer(required=True,description='Individual parent_male_id'),
#     'parent_female_id' : fields.Integer(required=True,description='Individual parent_female_id'),
#     'birth_rank' : fields.Integer(required=True,description='Individual birth_rank'),
#     'dead' : fields.Boolean(required=True,description='Individual dead'),
#     'youngdead' : fields.Boolean(required=True,description='Individual youngdead'),
#     'birth_date' : fields.String(required=True,description='Individual birth_date'),
#     'birth_place' : fields.String(required=True,description='Individual birth_place'),
#     'email' : fields.String(required=True,description='Individual email'),
#     'telephone' : fields.String(required=True,description='Individual telephone'),
#     'profession' : fields.String(required=True,description='Individual profession'),
#     'country' : fields.String(required=True,description='Individual country'),
#     'city' : fields.String(required=True,description='Individual city'),
#     'linkedin' : fields.String(required=True,description='Individual linkedin'),
#     'twitter' : fields.String(required=True,description='Individual twitter'),
#     'facebook' : fields.String(required=True,description='Individual facebook'),
#     'instagram' : fields.String(required=True,description='Individual instagram'),
#     'aboutme' : fields.String(required=True,description='Individual aboutme'),
#     'isIncomingSpouse' : fields.Boolean(required=True,description='Individual isIncomingSpouse'),
#     'sFatherName' : fields.String(required=True,description='Individual sFatherName'),
#     'sFatherDead' : fields.Boolean(required=True,description='Individual sFatherDead'),
#     'sMotherName' : fields.String(required=True,description='Individual sMotherName'),
#     'sMotherDead' : fields.Boolean(required=True,description='Individual sMotherDead'),
#     'photoName' : fields.String(required=True,description='Individual photoName'),
#     'photoPath' : fields.String(required=True,description='Individual photoPath'),
#     'uploadPhoto': fields.Raw(required=True, description='Individual uploadPhoto', type='file'),  # Add this line
#     'spouseValues': fields.List(fields.String, required=True, description='Individual spouseValues'),  # Add this line
# })