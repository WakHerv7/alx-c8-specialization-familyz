from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api, app
from werkzeug.utils import secure_filename
from app.models import db
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like
from app.schemas.post import ns, post_schema, post_model
from app.helpers import is_iterable, is_valid_date, lifeValue, create_individual, process_parents, \
    process_generations, getFirst2Initials, lifeStatusFrontend, genderFrontend, str_to_bool, get_ids
from app.models.individual import Individual

import json, os, time, random
from PIL import Image

date_format = "%Y-%m-%d"
document_root = app.config['UPLOAD_FOLDER']
posts_root = app.config['UPLOAD_FOLDER']+'/posts'

# ns = api.namespace('posts', description='Post operations')

# LIST ALL ---------------------------------------
@ns.route('/')
class PostList(Resource):
    @ns.doc('list_posts')
    @ns.marshal_list_with(post_model)
    def get(self):
        posts = Post.query.all()
        posts_as_dict_list = []
        for post in posts:
            individual = Individual.query.get(post.author_id)
            post_to_dict = post.to_dict()
            post_to_dict['author'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            post_likes = Like.find_by_post_id(post.id)
            post_comments = Comment.find_by_post_id(post.id)
            post_to_dict["likes"] = [] if post_likes == None else [{"id":pl.id, "liked_by_id":pl.liked_by_id} for pl in post_likes]
            post_to_dict["comments"] = [] if post_comments == None else [{"id":pc.id, "content":pc.content, "author_id":pc.author_id} for pc in post_comments]
            # post_to_dict['author'] = post.author
            posts_as_dict_list.append(post_to_dict)
        
        return posts_as_dict_list

# GET ONE ---------------------------------------
@ns.route('/<int:id>')
class PostDetails(Resource):
    @ns.doc('get_post')
    @ns.marshal_with(post_model)
    def get(self, id):
        post = Post.query.get(id)
        if post:            
            individual = Individual.query.get(post.author_id)
            post_to_dict = post.to_dict()
            post_to_dict['author'] = {
                "id":individual.id,
                "myPhoto": individual.photoPath,
                "myPhotoName": individual.photoName,
                "myName": individual.name,
                "myGender": individual.gender,
                "myLifeStatus": lifeStatusFrontend(individual.dead, individual.youngdead),
            }
            post_likes = Like.find_by_post_id(post.id)
            post_comments = Comment.find_by_post_id(post.id)
            post_to_dict["likes"] = [] if post_likes == None else [pl.id for pl in post_likes]
            post_to_dict["comments"] = [] if post_comments == None else [{"id":pc.id, "content":pc.content} for pc in post_comments]
            # post_to_dict['author'] = post.author
            return post_to_dict        
        return {"error": "Post not found"}, 404

# CREATE ---------------------------------------
@ns.route('/add')
class PostCreate(Resource):
    @ns.doc('create_post')
    @ns.expect(post_schema)
    @ns.marshal_with(post_model, code=201)
    def post(self):
        args = post_schema.parse_args()
        title = args['title']
        content = args['content']
        picture = args['picture']
        author_id= args['author_id']

        post = Post(title=title, content=content, author_id=author_id)
        # individual = Individual.query.get(author_id)
        # if individual:
        #     post.author = individual

        if picture:            
            timestr = time.strftime("%Y%m%d-%H%M%S")
            photoName = 'Photo-'+timestr+".jpg"                
            pathToConvertedFiles = os.path.join(posts_root, photoName)
            img = Image.open(picture)
            img = img.convert('RGB')
            img.thumbnail((1024, 1024))
            img.save(pathToConvertedFiles)
            post.picture_name = photoName 
            post.picture_path = pathToConvertedFiles
        
        post.save()

        return post.to_dict(), 201

# UPDATE ---------------------------------------
@ns.route('/update/<int:id>')
class PostUpdate(Resource):
    @ns.doc('update_post')
    @ns.expect(post_schema)
    @ns.marshal_with(post_model)
    def put(self, id):
        if not id or id != 0:
            post = Post.query.get(id)
            if post:
                args = post_schema.parse_args()
                title = args['title']
                content = args['content']
                picture = args['picture']
                author_id= args['author_id']
                
                post.title = title
                post.content = content
                post.author_id = author_id
                
                if picture:
                    # Delete the old file if it exists
                    old_filename = args['picture_name']
                    if old_filename and os.path.exists(os.path.join(posts_root, old_filename)):
                        os.remove(os.path.join(posts_root, old_filename))
                    
                    timestr = time.strftime("%Y%m%d-%H%M%S")
                    photoName = 'Photo-'+timestr+".jpg"                
                    pathToConvertedFiles = os.path.join(posts_root, photoName)
                    img = Image.open(picture)
                    img = img.convert('RGB')
                    img.thumbnail((1024, 1024))
                    img.save(pathToConvertedFiles)
                    post.picture_name = photoName 
                    post.picture_path = pathToConvertedFiles

                post.save()
                return post.to_dict()
        return {"error": "Invalid ID"}, 400

# DELETE ---------------------------------------
@ns.route('/delete/<int:id>')
class PostDelete(Resource):
    @ns.doc('delete_post')
    @ns.response(204, 'Post deleted')
    def delete(self, id):
        if not id or id != 0:
            post = Post.query.get(id)
            if post:
                db.session.delete(post)
                db.session.commit()
                return '', 204
        return {"error": "Invalid ID"}, 400
    


#ERROR HANDLER ---------------------------------------
@api.errorhandler(Exception)
def handle_error(e):
    return {"message": "An unexpected error occurred: " + str(e)}, 500
