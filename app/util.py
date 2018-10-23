from flask import jsonify
from app.code import Code

def make_result(data=None, code= Code.SUCCESS):
    return jsonify({"code": code, "data": data, "msg": Code.msg[code]})