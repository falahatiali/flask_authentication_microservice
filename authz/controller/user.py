from flask import request,abort


class UserController:
    def create_user():
        return "user created"
    
    def get_users():
        return "get users 1"

    def get_user():
        return "get user"

    def update_user():
        return "update user"

    def delete_user():
        return "delete a user"        
