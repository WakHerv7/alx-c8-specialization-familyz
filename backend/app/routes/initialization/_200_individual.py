from app.models.individual import Individual
from app.models.family import Family
import json, os, time, random
from PIL import Image
from datetime import datetime, date
from app.helpers import date_format, is_iterable, is_valid_date, lifeValue, \
    lifeValue, create_individual, process_parents, process_generations, \
    getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids

from app import app
from app.models import db

photos_root = app.config['UPLOAD_FOLDER']+'/photos'

def init_individuals(individualsList):
    for item in individualsList:
        def get_arg(key):
            return item[key]
        
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
            is_ghost = str_to_bool(get_arg('is_ghost')),
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

            cmo.set_spouses(SVs)

        if get_arg('families'):
            individual_families = []
            for fmlyID in json.loads(get_arg('families')):
                fmly = Family.query.get(int(fmlyID))
                individual_families.append(fmly)

            cmo.set_families(individual_families)

        # cmo.save()
        db.session.add(cmo)
    db.session.commit()







individualsList = [
    { 
        'currentMemberId': None,
        'urlLastButOneItem': None,
        'myName': "James Kingsley",
        'myUsername': "james.k",
        'myGender': 'm',
        'myLifeStatus': 'alive',
        'isIncomingSpouse': 'false',
        'noPhotoCheck': 'true',
        'uploadedPhotoName': '',
        'uploadedPhoto': '',
        'fatherId': None,
        'newFatherCheck': 'false',
        'newFatherName': '',
        'hasFatherCheck': 'false',
        'fatherLifeStatusValue': '',
        'motherId': None,
        'newMotherCheck': 'false',
        'newMotherName': '',
        'hasMotherCheck': 'false',
        'motherLifeStatusValue': '',
        'spouseValues': '',
        'families': '[1]',
        'birthdate': '2000-01-07',
        'birthplace': '',
        'birthrank': '',
        'email': 'james.kingsley@email.com',
        'telephone': '',
        'profession': '',
        'country': '',
        'city': '',
        'linkedin': '',
        'twitter': '',
        'facebook': '',
        'instagram': '',
        'aboutme': '',
        "is_ghost": 'false',
        "is_deleted": 'false',
    },
    { 
        'currentMemberId': None,
        'urlLastButOneItem': None,
        'myName': "Theresa Nwankwo",
        'myUsername': "theresa.n",
        'myGender': 'f',
        'myLifeStatus': 'alive',
        'isIncomingSpouse': 'false',
        'noPhotoCheck': 'true',
        'uploadedPhotoName': '',
        'uploadedPhoto': '',
        'fatherId': None,
        'newFatherCheck': 'false',
        'newFatherName': '',
        'hasFatherCheck': 'false',
        'fatherLifeStatusValue': '',
        'motherId': None,
        'newMotherCheck': 'false',
        'newMotherName': '',
        'hasMotherCheck': 'false',
        'motherLifeStatusValue': '',
        'spouseValues': '[1]',
        'families': '[2]',
        'birthdate': '2002-03-27',
        'birthplace': '',
        'birthrank': '',
        'email': 'theresa.nwankwo@email.com',
        'telephone': '',
        'profession': '',
        'country': '',
        'city': '',
        'linkedin': '',
        'twitter': '',
        'facebook': '',
        'instagram': '',
        'aboutme': '',
        "is_ghost": 'false',
        "is_deleted": 'false',
    },
    { 
        'currentMemberId': None,
        'urlLastButOneItem': None,
        'myName': "Brandon Kingsley",
        'myUsername': "brandon.k",
        'myGender': 'm',
        'myLifeStatus': 'alive',
        'isIncomingSpouse': 'false',
        'noPhotoCheck': 'true',
        'uploadedPhotoName': '',
        'uploadedPhoto': '',
        'fatherId': 1,
        'newFatherCheck': 'false',
        'newFatherName': '',
        'hasFatherCheck': 'true',
        'fatherLifeStatusValue': '',
        'motherId': 2,
        'newMotherCheck': 'false',
        'newMotherName': '',
        'hasMotherCheck': 'true',
        'motherLifeStatusValue': '',
        'spouseValues': '',
        'families': '[1,2]',
        'birthdate': '2020-05-10',
        'birthplace': '',
        'birthrank': '',
        'email': 'brandon.k@email.com',
        'telephone': '',
        'profession': '',
        'country': '',
        'city': '',
        'linkedin': '',
        'twitter': '',
        'facebook': '',
        'instagram': '',
        'aboutme': '',
        "is_ghost": 'false',
        "is_deleted": 'false',
    },
    { 
        'currentMemberId': None,
        'urlLastButOneItem': None,
        'myName': "Clara Kingsley",
        'myUsername': "clara.k",
        'myGender': 'f',
        'myLifeStatus': 'alive',
        'isIncomingSpouse': 'false',
        'noPhotoCheck': 'true',
        'uploadedPhotoName': '',
        'uploadedPhoto': '',
        'fatherId': 1,
        'newFatherCheck': 'false',
        'newFatherName': '',
        'hasFatherCheck': 'true',
        'fatherLifeStatusValue': '',
        'motherId': 2,
        'newMotherCheck': 'false',
        'newMotherName': '',
        'hasMotherCheck': 'true',
        'motherLifeStatusValue': '',
        'spouseValues': '',
        'families': '[1,2]',
        'birthdate': '2021-07-20',
        'birthplace': '',
        'birthrank': '',
        'email': 'clara.k@email.com',
        'telephone': '',
        'profession': '',
        'country': '',
        'city': '',
        'linkedin': '',
        'twitter': '',
        'facebook': '',
        'instagram': '',
        'aboutme': '',
        "is_ghost": 'false',
        "is_deleted": 'false',
    },
    { 
        'currentMemberId': None,
        'urlLastButOneItem': None,
        'myName': "Jonathan Kingsley",
        'myUsername': "jonathan.k",
        'myGender': 'm',
        'myLifeStatus': 'alive',
        'isIncomingSpouse': 'false',
        'noPhotoCheck': 'true',
        'uploadedPhotoName': '',
        'uploadedPhoto': '',
        'fatherId': 1,
        'newFatherCheck': 'false',
        'newFatherName': '',
        'hasFatherCheck': 'true',
        'fatherLifeStatusValue': '',
        'motherId': 2,
        'newMotherCheck': 'false',
        'newMotherName': '',
        'hasMotherCheck': 'true',
        'motherLifeStatusValue': '',
        'spouseValues': '',
        'families': '[1,2]',
        'birthdate': '2021-10-03',
        'birthplace': '',
        'birthrank': '',
        'email': 'jonathan.k@email.com',
        'telephone': '',
        'profession': '',
        'country': '',
        'city': '',
        'linkedin': '',
        'twitter': '',
        'facebook': '',
        'instagram': '',
        'aboutme': '',
        "is_ghost": 'false',
        "is_deleted": 'false',
    },
    
] 