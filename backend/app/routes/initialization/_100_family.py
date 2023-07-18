from app.models.family import Family
from app.models import db

def init_families(familiesList):
    for item in familiesList:
        family = Family(name=item['name'])
        family.save()
    #     db.session.add(family)
    # db.session.commit()







familiesList = [
    { 
        "name":"Kingsley family",
    },
    { 
        "name":"Nwankwo family",
    },
    # { 
    #     "name":"Adenuga family",
    # },
    # { 
    #     "name":"Maxwell family",
    # },
] 