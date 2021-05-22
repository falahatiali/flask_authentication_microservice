from flask import abort,request

from authz.model import User
from authz.schema import UserSchema
from authz.config import Config
from authz.util import now
from authz import db

from time import time
from jwt import encode


class AuthTokenController:

    def create_jwt_token():
        if request.content_type != 'application/json':
            abort(415) #Bad media type
        user_schema = UserSchema(only=["username" ,"password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            abort(400)

        if not data["username"] or not data["password"]:
            abort(400)
        try:
            user = User.query.filter_by(username=data["username"]).first()
        except:
            abort(500) #user not found
        
        if user is None:
            abort(404)
        
        if user.password != data["password"]:
            user.last_failed_at = now()
            try:
                db.session.commit()
            except:
                db.session.rollback()
                abort(500)
            abort(403)
        
        current_time = time()

        try:
            jwt_token = encode(
                {
                    "nbf": current_time,
                    "exp": current_time + Config.JWT_TOKEN_LIFETIME,
                    "user":{
                        "id": user.id,
                        "username":user.username,
                        "role": user.role
                    }
                }, 
                Config.AUTHZ_SECRET,
                algorithm=Config.JWT_ALGO
            ) # Create new jwt token
        except:
            abort(500) # Exception in encoding jwt
        
        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        } ,201, {"X-Subject-Token": jwt_token}