"""
状态码管理
"""


class Code:
    SUCCESS = 200
    AUTHERROR = 405
    NO_PARAM = 202
    ACCOUNT_NOFOUND = 249
    LOGIN_FAILED = 250
    
    msg = {
        SUCCESS: "成功",
        NO_PARAM: "参数错误",
        AUTHERROR: "无权限当前操作",
        ACCOUNT_NOFOUND: "该账号未注册",
        LOGIN_FAILED: "账号密码不正确,登录失败"
    }