from app.models.individual import Individual
from datetime import datetime
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

date_format = "%Y-%m-%d"


@login_manager.user_loader
def load_user(individual_id):
    return Individual.query.get(int(individual_id))

def hash_password(password):
    # For Werkzeug
    return generate_password_hash(password)

def check_password(hashed_password, password):
    # For Werkzeug
    return check_password_hash(hashed_password, password)


# ================================================================

def str_to_bool(bool_str):
    return bool_str.lower() == 'true' if bool_str else False

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def is_valid_date(date_string, date_format='Y-m-d'):
    if date_string :
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
    return False

def get_ids(obj_list):
    return [obj['id'] for obj in obj_list]

def lifeValueFr(data):
    deadValue = False
    youngdeadValue = False
    
    if data == 'vie':
        deadValue = False
    elif data == 'mort':
        deadValue = True
    elif data == 'mba':
        deadValue = True
        youngdeadValue = True

    return {"dv": deadValue, "ydv":youngdeadValue}

def lifeValue(data):
    deadValue = False
    youngdeadValue = False
    
    if data == 'alive':
        deadValue = False
    elif data == 'dead':
        deadValue = True
    elif data == 'daya':
        deadValue = True
        youngdeadValue = True

    return {"dv": deadValue, "ydv":youngdeadValue}


def getFirst2Initials(name) :
    w = ''
    namesTab = name.split(' ')
    for idx,item  in enumerate(namesTab):
        if idx < 2:
            w = w + namesTab[idx][0]
    w = w.upper()
    return w


def lifeStatusFrontend(dv, ydv, gend=None):
    if gend == None : 
        if dv == False:
            return 'alive'
        elif dv == True:
            if ydv == False:
                return 'dead'
            else:
                return 'daya'
    elif gend == 'm':
        if dv == False:
            return 'Alive'
        elif dv == True:
            if ydv == False:
                return 'Deceased'
            else:
                return 'Deceased at young age'
    elif gend == 'f':
        if dv == False:
            return 'Alive'
        elif dv == True:
            if ydv == False:
                return 'Deceased'
            else:
                return 'Deceased at young age'

def lifeStatusFrontendFr(dv, ydv, gend=None):
    if gend == None : 
        if dv == False:
            return 'vie'
        elif dv == True:
            if ydv == False:
                return 'mort'
            else:
                return 'mba'
    elif gend == 'm':
        if dv == False:
            return 'En vie'
        elif dv == True:
            if ydv == False:
                return 'Mort'
            else:
                return 'Mort à bas âge'
    elif gend == 'f':
        if dv == False:
            return 'En vie'
        elif dv == True:
            if ydv == False:
                return 'Morte'
            else:
                return 'Morte à bas âge'
            
def genderFrontend(gend):
    if gend == 'm':
       return 'Male' 
    elif gend == 'f':
        return 'Female'
    
def genderFrontendFr(gend):
    if gend == 'm':
       return 'Masculin' 
    elif gend == 'f':
        return 'Feminin'
    

def create_individual(name, gender, life_status_value):
    lv = lifeValue(life_status_value)
    indiv = Individual(
        name=name,
        gender=gender,
        dead=lv["dv"],
        youngdead=lv["ydv"]
    )
    indiv.save()
    return indiv.id

def process_parents(has_check, new_check, url_check, id_value, new_name, life_status_value, gender):
    if not has_check:
        return None
    elif new_check and url_check != 'new_spouse':
        return create_individual(new_name, gender, life_status_value)
    else:
        return id_value
    

def process_generations(family, family_generations):
    unsolved_generations = any(member["generation"] is None for member in family)

    fgi = 0
    while unsolved_generations:
        new_gen = []
        for indfam in family:
            for ig0 in family_generations[fgi]:
                current_indiv = next(
                    (item for item in family if item["id"] == ig0), None
                )
                if indfam["father"]["id"] == ig0 or indfam["mother"]["id"] == ig0:
                    indfam["generation"] = current_indiv["generation"] + 1
                    new_gen.append(indfam["id"])
                    if indfam["spouses"]:
                        for isp in indfam["spouses"]:
                            spouse_item = next(
                                (item for item in family if item["id"] == isp["id"]), None
                            )
                            spouse_item["generation"] = current_indiv["generation"] + 1
                            new_gen.append(spouse_item["id"])

        new_gen = list(dict.fromkeys(new_gen))
        family_generations.append(new_gen)
        unsolved_generations = any(member["generation"] is None for member in family)
        if unsolved_generations:
            fgi += 1

    nb_gen = len(family_generations)
    largest_gen = {"rank": 0, "size": 0}
    for index, fg in enumerate(family_generations):
        if len(fg) >= largest_gen["size"]:
            largest_gen["rank"] = index
            largest_gen["size"] = len(fg)

    return family_generations, nb_gen, largest_gen