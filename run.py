"""
运行入口
"""

from flask import Flask, abort
import flask_restful
from app.util import make_result
from app.code import Code
from apiController import api


app = Flask(__name__)

app.register_blueprint(api)


def custom_abort(http_status_code, *args, **kwargs):
    """
    改写参数传递错误的返回格式
    :param http_status_code: 状态码
    :param args:
    :param kwargs:
    :return: 定义返回data
    """
    if http_status_code == 400:
        abort(make_result(code=Code.NO_PARAM))
    return abort(http_status_code)


flask_restful.abort = custom_abort


if __name__ == "__main__":
    app.run(port=8811, debug=True)