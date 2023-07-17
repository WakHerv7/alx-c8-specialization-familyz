from flask import Blueprint, request, redirect, jsonify, render_template
# from flask import Flask
from flask_restx import Resource, Api, fields
from app import api
from app.models import db
from app.models.entry import Entry
from app.models.individual import Individual
# from app.schemas.entry import entry_schema
from app.schemas.auth import signup_schema, signin_schema
from app.helpers import hash_password, check_password
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

import json

ns = api.namespace('auth', description='Authentication operations')

# SIGN UP ---------------------------------------
@ns.route('/signup')
class UserSignup(Resource):
    # @ns.doc('sign_up')
    @ns.expect(signup_schema)
    # @ns.marshal_with(signup_schema, code=201)
    def post(self):
        data = api.payload
        name = data['name']
        email = data['email']
        password = data['password']
        birthdate = data['birthdate']
        birthplace = data['birthplace']
        telephone = data['telephone']
        profession = data['profession']
        country = data['country']
        city = data['city']
        
        # Check if the user already exists in your database
        individual = Individual.query.filter_by(email=email).first()
        # If not, save the hashed password and other details in the database
        if not individual :            
            hashed_password = hash_password(password)
            user = Individual(
                name = name,
                email = email,
                password = hashed_password,
                birthdate = birthdate,
                birthplace = birthplace,
                telephone = telephone,
                profession = profession,
                country = country,
                city = city
            )
            user.save()
            return {"status": "success", "message": "User registered"}, 201
        
        else:
            return {"status": "failed", "message": "'A user is already registered with this email'"}, 403
        


# SIGN IN ---------------------------------------
@ns.route('/signin')
class UserSignin(Resource):
    # @ns.doc('sign_in')
    @ns.expect(signin_schema)
    # @ns.marshal_with(signin_schema, code=201)
    def post(self):
        data = api.payload
        email = data['email']
        password = data['password']
        
        # Check if the user exists in your database
        user = Individual.query.filter_by(email=email).first()
        # If the user exists, compare the hashed password
        if user and check_password(user.password, password):
            # login_user(user)
            return {"status": "success", "message": "Authenticated"}, 200
        else:
            return {"status": "failure", "message": "Authentication failed"}, 401


# SIGN OUT ---------------------------------------
# @ns.route('/signout')
# class UserSignout(Resource):
#     def post(self):

