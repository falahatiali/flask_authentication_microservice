from flask_restful import Resource

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return "users"
        else:
            return "user"
    
    def post(self):
        return "user created"
    
    def patch(self):
        return "used updated"
    