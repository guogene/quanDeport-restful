"""
接口控制器
"""

from flask_restful import Resource, abort
from app.code import Code
from apiModels.UserModel import User
from app.util import make_result
from .parser import IdTestApi, NameTestApi, LoginApi
from .token_auth import auth


class Test(Resource):
    
    def get(self):
        req = IdTestApi().rep.parse_args(strict=True)
        id = req.get('id')
        return make_result(data={"id": id*123})


class PostTest(Resource):

    @auth.login_required
    def post(self):
        rep = NameTestApi().rep.parse_args(strict=True)
        name = rep.get('name')
        return make_result(data={"name": name + "--真实玩家"})


class Login(Resource):
    
    def post(self):
        rep = LoginApi().rep.parse_args(strict=True)
        user_name = rep.get('user_name')
        password = rep.get('password')
        user = User.query.filter_by(user_name=user_name).first()
        if user is None:
            abort(make_result(code=Code.ACCOUNT_NOFOUND))
        elif user.check_password(password) is False:
            abort(make_result(code=Code.LOGIN_FAILED))
        else:
            return make_result(data={"token": 'this_is_token_1'})