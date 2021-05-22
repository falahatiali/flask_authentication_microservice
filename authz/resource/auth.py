from flask_restful import Resource
from authz.controller import AuthTokenController


class AuthTokenResource(Resource):

     def post(self):
         return AuthTokenController.create_jwt_token()
