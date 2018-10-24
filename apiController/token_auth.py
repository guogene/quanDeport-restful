"""
页面TOKEN权限管理
"""
from flask import g, abort
from flask_httpauth import HTTPTokenAuth
from app.code import Code
from app.util import make_result
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

SECRET_KEY = 'LXDJEOX,SOEFHISO13'
EXPIRATION_TIME = 3600
auth = HTTPTokenAuth(scheme="Token-")

tokens = {
    'this_is_token_1': 'xin'
}

def generate_auth_token(user_id, expiration = EXPIRATION_TIME):
    s = Serializer(SECRET_KEY, expires_in=expiration)
    return s.dumps({'user_id': user_id})

@auth.verify_token
def verify_token(token):
    s = Serializer(SECRET_KEY, expires_in=EXPIRATION_TIME)
    try:
        data = s.loads(token)
        g.user_id = data['user_id']
        return True
    except SignatureExpired:
        abort(make_result(code=Code.EXPIRED_TOKEN))  # valid token, but expired
    except BadSignature:
        abort(make_result(code=Code.INVALID_TOKEN))  # invalid token

@auth.error_handler
def verify_error():
    abort(make_result(code=Code.AUTH_ERROR))
    