"""
对接口的参数进行定义
"""
from flask_restful.reqparse import RequestParser


class IdTestApi:
    def __init__(self):
        self.rep = RequestParser()
        self.rep.add_argument("id", type=int, location="args", required=True)
        super(IdTestApi, self).__init__()


class NameTestApi:
    def __init__(self):
        self.rep = RequestParser()
        self.rep.add_argument("name", type=str, location="json", required=False)
        super(NameTestApi, self).__init__()

class LoginApi:
    def __init__(self):
        self.rep = RequestParser()
        self.rep.add_argument("user_name", type=str, location="json", required=True)
        self.rep.add_argument("password", type=str, location="json", required=True)
        super(LoginApi, self).__init__()