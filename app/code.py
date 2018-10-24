"""
状态码管理
"""


class Code:
    SUCCESS = 200
    NO_PARAM = 202
    EXPIRED_TOKEN = 203
    INVALID_TOKEN = 204
    ACCOUNT_NOFOUND = 249
    LOGIN_FAILED = 250
    AUTH_ERROR = 405
    
    msg = {
        SUCCESS: "成功",
        NO_PARAM: "参数错误",
        AUTH_ERROR: "无权限当前操作",
        ACCOUNT_NOFOUND: "该账号未注册",
        LOGIN_FAILED: "账号密码不正确,登录失败",
        EXPIRED_TOKEN: "TOKEN,已经过期请重新申请",
        INVALID_TOKEN: "非法TOKEN!"
    }