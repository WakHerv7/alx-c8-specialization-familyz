from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# def NewFamilyMember(request, document_root):
#     if request.method == 'POST':
#         currentMemberId = request.POST['currentMemberId']
#         urlLastButOneItem = request.POST['urlLastButOneItem']
#         myName = request.POST['myName']
#         myGender = request.POST['myGender']
#         myLifeStatus = request.POST['myLifeStatus']
#         isIncomingSpouse = request.POST['isIncomingSpouse']
#         noPhotoCheck = False if request.POST['noPhotoCheck'] == 'false' else True
#         uploadedPhotoName = request.POST['uploadedPhotoName']
#         uploadedPhoto = request.FILES['uploadedPhoto'] if uploadedPhotoName != 'undefined' else False
#         fatherId = request.POST['fatherId']
#         newFatherCheck = request.POST['newFatherCheck']
#         newFatherName = request.POST['newFatherName']
#         hasFatherCheck = request.POST['hasFatherCheck']
#         fatherLifeStatusValue = request.POST['fatherLifeStatusValue']
#         motherId = request.POST['motherId']
#         newMotherCheck = request.POST['newMotherCheck']
#         newMotherName = request.POST['newMotherName']
#         hasMotherCheck = request.POST['hasMotherCheck']
#         motherLifeStatusValue = request.POST['motherLifeStatusValue']
#         spouseValues = request.POST['spouseValues']
#         birthdate = request.POST['birthdate']
#         birthplace = request.POST['birthplace']
#         birthrank = request.POST['birthrank']
#         email = request.POST['email']
#         telephone = request.POST['telephone']
#         profession = request.POST['profession']
#         country = request.POST['country']
#         city = request.POST['city']
#         linkedin = request.POST['linkedin']
#         twitter = request.POST['twitter']
#         facebook = request.POST['facebook']
#         instagram = request.POST['instagram']
#         aboutme = request.POST['aboutme']
#         if hasFatherCheck == 'false':
#             fatherId = None        
#         elif newFatherCheck == 'true' and urlLastButOneItem != 'new_spouse':
#             lv = lifeValue(fatherLifeStatusValue)
#             indiv = Individu(
#                 name = newFatherName,
#                 gender = 'm',
#                 dead = lv["dv"],
#                 youngdead = lv["ydv"]
#             )
#             indiv.save() 
#             fatherId = indiv.id
#         elif hasFatherCheck == 'false' and newFatherCheck != 'true':
#             fatherId = None
#         if hasMotherCheck == 'false':
#             motherId = None
#         elif newMotherCheck == 'true' and urlLastButOneItem != 'new_spouse':            
#             lv = lifeValue(motherLifeStatusValue)
#             indiv = Individu(
#                 name = newMotherName,
#                 gender = 'f',
#                 dead = lv["dv"],
#                 youngdead = lv["ydv"]
#             )
#             indiv.save() 
#             motherId = indiv.id
#         elif hasMotherCheck == 'false' and newMotherCheck != 'true' :
#             motherId = None
#         my_lv = lifeValue(myLifeStatus)
#         # Modify family member
#         if currentMemberId != 'null' and urlLastButOneItem == 'update_item':
#             cmo = Individu.objects.get(id=currentMemberId)
#             cmo.name = myName
#             cmo.gender = myGender
#             cmo.dead = my_lv["dv"]
#             cmo.youngdead = my_lv["ydv"]
#             cmo.generation = None
#             cmo.parent_male_id = fatherId
#             cmo.parent_female_id = motherId
#             cmo.birth_rank = None if birthrank == '' else birthrank
#             cmo.birth_date = None if birthdate == '' else birthdate
#             cmo.birth_place = birthplace
#             cmo.email = email
#             cmo.telephone = telephone
#             cmo.profession = profession
#             cmo.country = country
#             cmo.city = city
#             cmo.linkedin = linkedin
#             cmo.twitter = twitter
#             cmo.facebook = facebook
#             cmo.instagram = instagram
#             cmo.aboutme = aboutme
#             if cmo.isIncomingSpouse :
#                 cmo.sFatherName = newFatherName
#                 cmo.sMotherName = newMotherName
#                 mlv = lifeValue(motherLifeStatusValue)
#                 flv = lifeValue(fatherLifeStatusValue)
#                 cmo.sFatherDead = flv["dv"]
#                 cmo.sMotherDead = mlv["dv"]
#             if noPhotoCheck:
#                 cmo.photoName = None
#                 cmo.photoPath.delete()
#             else:
#                 if uploadedPhoto:
#                     if cmo.photoPath:
#                         cmo.photoPath.delete()                
#                     timestr = time.strftime("%Y%m%d-%H%M%S")
#                     photoName = 'Photo-'+timestr+".jpg"                
#                     pathToConvertedFiles = os.path.join(document_root,'photos', photoName)
#                     relativePathToConvertedFiles = os.path.join('photos', photoName)
#                     img = Image.open(uploadedPhoto)
#                     img = img.convert('RGB')
#                     img.thumbnail((256, 256))
#                     img.save(pathToConvertedFiles)                
#                     cmo.photoName = photoName
#                     cmo.photoPath.name = relativePathToConvertedFiles
#             # ######################
#             SVs = []
#             for sve in json.loads(spouseValues):
#                 if sve["newConjointCheck"] == 'true':
#                     lv = lifeValue(sve["status"])
#                     indiv = Individu(
#                         name = sve["newConjointName"],
#                         gender = sve["gender"],
#                         dead = lv["dv"],
#                         youngdead = lv["ydv"]
#                     )
#                     indiv.save()
#                     SVs.append(indiv.id)
#                 else:
#                     SVs.append(int(sve["conjointId"]))
#             cmo.spouses.set(SVs)            
#             cmo.save()
#             # ######################
#         else:
#             # Create a new family member
#             fm = Individu(
#                 name = myName,
#                 gender = myGender,
#                 dead = my_lv["dv"],
#                 youngdead = my_lv["ydv"],
#                 generation = None,
#                 parent_male_id = fatherId,
#                 parent_female_id = motherId,
#                 birth_rank = None if birthrank == '' else birthrank,
#                 birth_date = None if birthdate == '' else birthdate,
#                 birth_place = birthplace,
#                 email = email,
#                 telephone = telephone,
#                 profession = profession,
#                 country = country,
#                 city = city,
#                 linkedin = linkedin,
#                 twitter = twitter,
#                 facebook = facebook,
#                 instagram = instagram,
#                 aboutme = aboutme,
#                 isIncomingSpouse = False if isIncomingSpouse == 'false' else True,                             
#             )
#             if urlLastButOneItem == 'new_spouse' :
#                 fm.isIncomingSpouse = True
#                 fm.sFatherName = newFatherName
#                 fm.sMotherName = newMotherName
#                 mlv = lifeValue(motherLifeStatusValue)
#                 flv = lifeValue(fatherLifeStatusValue)
#                 fm.sFatherDead = flv["dv"]
#                 fm.sMotherDead = mlv["dv"]            
#             if not(noPhotoCheck) and uploadedPhoto:
#                 timestr = time.strftime("%Y%m%d-%H%M%S")
#                 photoName = 'Photo-'+timestr+".jpg"
#                 pathToConvertedFiles = os.path.join(document_root,'photos', photoName)
#                 relativePathToConvertedFiles = os.path.join('photos', photoName)
#                 img = Image.open(uploadedPhoto)
#                 img = img.convert('RGB')
#                 img.thumbnail((256, 256))
#                 img.save(pathToConvertedFiles)
#                 fm.photoName = photoName
#                 fm.photoPath.name = relativePathToConvertedFiles                
#             fm.save()      
#             # ######################
#             SVs = []
#             for sv in json.loads(spouseValues):
#                 if sv["newConjointCheck"] == 'true':
#                     lv = lifeValue(sv["status"])
#                     indiv = Individu(
#                         name = sv["newConjointName"],
#                         gender = sv["gender"],
#                         dead = lv["dv"],
#                         youngdead = lv["ydv"]
#                     )
#                     indiv.save()
#                     SVs.append(indiv.id)
#                 else:
#                     SVs.append(int(sv["conjointId"]))
#             fm.spouses.set(SVs)
#             fm.save()
#         return JsonResponse({"message": "Success"}, status = 200)
#     else:
#         return render(request, 'main/new_fm.html')
    




    