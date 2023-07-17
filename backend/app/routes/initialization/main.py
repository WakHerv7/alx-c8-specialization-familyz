
from app.models.individual import Individual
from app.models.family import Family
from flask_restx import Resource, Api, fields
from app import api
from app.schemas.individual import ns
#------------------------------------------------
from app.routes.initialization._100_family import familiesList, init_families
from app.routes.initialization._200_individual import individualsList, init_individuals
from app.routes.initialization._300_post import postsList, init_posts
from app.routes.initialization._400_comment import commentsList, init_comments
from app.routes.initialization._500_like import likesList, init_likes
#------------------------------------------------

ns = api.namespace('initialization', description='Initialization operations')

# INITIALIZE DATA ---------------------------------------
@ns.route('/initialize_data')
class InitializeData(Resource):
    @ns.doc('initialize_data')
    # @ns.marshal_with(individual_form_data_response)
    def get(self):
        indivs = Individual.query.all()
        fams = Family.query.all()
        if len(fams)==0 and len(indivs)==0 :
        # if True :
            init_families(familiesList)
            init_individuals(individualsList)
            init_posts(postsList)
            init_comments(commentsList)
            init_likes(likesList)

            return True
        
        return False





































