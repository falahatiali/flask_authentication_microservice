from authz import api
from authz.resource.user import UserResource

api.add_resource(
    UserResource , 
    "/users",
    methods=["GET" , "POST"],
    endpoint="users"
)

api.add_resource(
    UserResource,
    "/user",
    methods=["GET" , "PATCH" , "DELETE"],
    endpoint="user"
) 