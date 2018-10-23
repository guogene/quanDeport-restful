from .view import Test, PostTest, Login
from flask_restful import Api
from flask import Blueprint

api = Blueprint('api', __name__)
resource = Api(api)
resource.add_resource(Test, "/api")
resource.add_resource(PostTest, "/api/user")
resource.add_resource(Login, '/api/login')