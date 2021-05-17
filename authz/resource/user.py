from flask_restful import Resource
from authz.controller.user import UserController

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)
    
    def post(self):
        return UserController.create_user()
    
    def patch(self):
        return UserController.update_user()
    
    def delete_user(self):
        return UserController.delete_user()
    