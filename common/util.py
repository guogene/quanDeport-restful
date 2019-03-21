"""
常用方法
"""
from config import MYSQL_CONFIG


def create_mysql_uri(name):
    info = MYSQL_CONFIG.get(name, False)
    if not info:
        return '无该连接信息'
    base_uri = "mysql+pymysql://"
    user_uri = "%s:%s@%s:%s/%s?charset=utf8" % (info['user'], info['password'], info['host'],
                                                info['port'], info['database'])
    return base_uri + user_uri
