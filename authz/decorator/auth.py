from functools import wraps
from flask import abort, request
from authz.config import Config
from jwt import decode
from authz.rule import ControllerRule


def auth_required(f):
    @wraps(f)
    def wrapper(*args , **kwargs):
        jwt = request.headers.get("X-Auth-Token")
        if jwt is None:
            abort(401)
        try:
            data = decode(jwt , Config.AUTHZ_SECRET, algorithms=[Config.JWT_ALGO])
        except:
            abort(401)
        controller_roles = ControllerRule.get_controller_roles(f.__name__)
        if data["user"]["role"] in controller_roles:
            return f(*args , **kwargs)
        elif data["user"]["role"] == "member" and "member:user_id" in controller_roles:
            user_id = args[f.__code__.co_varnames.index("user_id")]
            if data["user"]["id"] == user_id:
                return f(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)

    return wrapper
