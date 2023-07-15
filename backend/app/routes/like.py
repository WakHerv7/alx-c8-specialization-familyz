from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api, app
from werkzeug.utils import secure_filename
from app.models import db
from app.models.like import Like
from app.models.post import Post
from app.schemas.like import ns, like_schema, like_model
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids
from app.models.individual import Individual

import json, os, time, random
from PIL import Image

date_format = "%Y-%m-%d"
document_root = app.config['UPLOAD_FOLDER']
likes_root = app.config['UPLOAD_FOLDER']+'/likes'

# ns = api.namespace('likes', description='Like operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class LikeList(Resource):
    @ns.doc('list_likes')
    @ns.marshal_list_with(like_model)
    def get(self):
        likes = Like.query.all()
        likes_as_dict_list =[]
        for like in likes:
            individual = Individual.query.get(like.liked_by_id)
            post = Post.query.get(like.post_id)
            like_to_dict = like.to_dict()
            like_to_dict['liked_by'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            like_to_dict['post'] = {
                "id":post.id,
                "title": post.title,
                "content": post.content,
            }
            likes_as_dict_list.append(like_to_dict)

        return likes_as_dict_list

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class LikeDetails(Resource):
    @ns.doc('get_like')
    @ns.marshal_with(like_model)
    def get(self, id):
        like = Like.query.get(id)
        if like:
            individual = Individual.query.get(like.liked_by_id)
            post = Post.query.get(like.post_id)
            like_to_dict = like.to_dict()
            like_to_dict['liked_by'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            like_to_dict['post'] = {
                "id":post.id,
                "title": post.title,
                "content": post.content,
            }

            return like_to_dict
        
        return {"error": "Like not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class LikeCreate(Resource):
    @ns.doc('create_like')
    @ns.expect(like_schema)
    @ns.marshal_with(like_model, code=201)
    def post(self):
        args = like_schema.parse_args()
        liked_by_id= args['liked_by_id']
        post_id= args['post_id']

        like = Like(liked_by_id=liked_by_id, post_id=post_id)
        
        like.save()
        return like.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class LikeUpdate(Resource):
    @ns.doc('update_like')
    @ns.expect(like_schema)
    @ns.marshal_with(like_model)
    def put(self, id):
        if not id or id != 0:
            like = Like.query.get(id)
            if like:
                args = like_schema.parse_args()
                liked_by_id= args['liked_by_id']
                post_id= args['post_id']
                
                like.liked_by_id = liked_by_id
                like.post_id = post_id
                
                # individual = Individual.query.get(args['liked_by_id'])
                # post = Post.query.get(args['post_id'])
                # if individual:
                #     like.liked_by = individual
                # if post:
                #     like.post = post

                like.save()
                return like.to_dict()
            
        return {"error": "Invalid ID"}, 400

# DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class LikeDelete(Resource):
    @ns.doc('delete_like')
    @ns.response(204, 'Like deleted')
    def delete(self, id):
        if not id or id != 0:
            like = Like.query.get(id)
            if like:
                db.session.delete(like)
                db.session.commit()
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500
