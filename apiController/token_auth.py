"""
页面TOKEN权限管理
"""
from flask import g, abort
from flask_httpauth import HTTPTokenAuth
from app.code import Code
from app.util import make_result

auth = HTTPTokenAuth(scheme="Token-")

tokens = {
    'this_is_token_1': 'xin'
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        g.current_user = tokens[token]
        return True
    return False

@auth.error_handler
def verify_error():
    abort(make_result(code=Code.AUTHERROR))
    