from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api, app
from werkzeug.utils import secure_filename
from app.models import db
from app.models.comment import Comment
from app.models.post import Post
from app.schemas.comment import ns, comment_schema, comment_model
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids
from app.models.individual import Individual

import json, os, time, random
from PIL import Image

date_format = "%Y-%m-%d"
document_root = app.config['UPLOAD_FOLDER']
comments_root = app.config['UPLOAD_FOLDER']+'/comments'

# ns = api.namespace('comments', description='Comment operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class CommentList(Resource):
    @ns.doc('list_comments')
    @ns.marshal_list_with(comment_model)
    def get(self):
        comments = Comment.query.all()
        comments_as_dict_list =[]
        for comment in comments:
            individual = Individual.query.get(comment.author_id)
            post = Post.query.get(comment.post_id)
            comment_to_dict = comment.to_dict()
            comment_to_dict['author'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            comment_to_dict['post'] = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
            }

            comments_as_dict_list.append(comment_to_dict)

        return comments_as_dict_list

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class CommentDetails(Resource):
    @ns.doc('get_comment')
    @ns.marshal_with(comment_model)
    def get(self, id):
        comment = Comment.query.get(id)
        if comment:
            individual = Individual.query.get(comment.author_id)
            post = Post.query.get(comment.post_id)
            comment_to_dict = comment.to_dict()
            comment_to_dict['author'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            comment_to_dict['post'] = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
            }

            return comment_to_dict 
               
        return {"error": "Comment not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class CommentCreate(Resource):
    @ns.doc('create_comment')
    @ns.expect(comment_schema)
    @ns.marshal_with(comment_model, code=201)
    def post(self):
        args = comment_schema.parse_args()
        content = args['content']
        author_id= args['author_id']
        post_id= args['post_id']

        comment = Comment(content=content, author_id=author_id, post_id=post_id)
        # individual = Individual.query.get(author_id)
        # post = Post.query.get(post_id)
        # if individual:
        #     comment.author = individual
        # if post:
        #     comment.post = post
        
        comment.save()
        return comment.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class CommentUpdate(Resource):
    @ns.doc('update_comment')
    @ns.expect(comment_schema)
    @ns.marshal_with(comment_model)
    def put(self, id):
        if not id or id != 0:
            comment = Comment.query.get(id)
            if comment:
                args = comment_schema.parse_args()
                content = args['content']
                author_id= args['author_id']
                post_id= args['post_id']
                
                comment.content = content
                comment.author_id = author_id
                comment.post_id = post_id
                comment.save()
                return comment.to_dict()
            
        return {"error": "Invalid ID"}, 400

# DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class CommentDelete(Resource):
    @ns.doc('delete_comment')
    @ns.response(204, 'Comment deleted')
    def delete(self, id):
        if not id or id != 0:
            comment = Comment.query.get(id)
            if comment:
                db.session.delete(comment)
                db.session.commit()
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500
