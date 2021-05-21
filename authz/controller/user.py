from flask import request,abort
from authz import db
from authz.model import User
from authz.schema import UserSchema


class UserController:
    def create_user():
        if request.content_type != 'application/json':
            abort(415)
        
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            abort(400)
        
        if not data["username"] or not data["password"]:
            abort(400)
        
        try:
            user = User.query.filter_by(username=data["username"]).first()
        except:
            abort(500)

        if user is not None:
            abort(409)

        user = User(username=data["username"], password=data["password"])
        db.session.add(user)

        try:
            db.session.commit() #Database create query
        except:
            db.session.rollback()
            abort(500)
        
        user_schema = UserSchema()

        return {
            "user": user_schema.dump(user)
        } ,201

    
    def get_users():
        try:
            users = User.query.all()
        except:
            abort(500)

        user_schema = UserSchema(many=True)
        return {
            "users": user_schema.dump(users)
        } ,200


    def get_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            abort(500)

        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        } ,200


    def update_user(user_id):
        if request.content_type != 'application/json':
            abort(415)
        
        user_schema = UserSchema(only=["password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            abort(404)
        if not data["password"]:
            abort(400)

        try:
            user = User.query.get(user_id) 
        except:
            abort(500)

        if user is None:
           abort(404)
        
        user.password = data["password"]
        try:
            db.session.commit() #Database UPDATE Query
        except:
            db.session.rollback()
            abort(500) #database error

        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        }, 200

        

    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            abort(500)

        if user is None:
            abort(404)
        try:
            db.session.delete(user) # Database delete query
        except:
            db.session.rollback()
            abort(500) # Database error

        db.session.commit()
        return "", 204
        
