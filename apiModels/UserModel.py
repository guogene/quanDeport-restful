from apiModels import db
from hashlib import md5


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.INT, primary_key=True)
    user_name = db.Column(db.String(99), unique=True)
    password = db.Column(db.String(255), unique=False)
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = self.hash_password(password)
    
    def __repr__(self):
        return '<User_id %r>' % self.id
    
    @staticmethod
    def hash_password(psw):
        """
        对明文密码加密
        :param psw:
        :return: md5_password
        """
        return md5(psw.encode("utf-8")).hexdigest()
    
    def check_password(self, psw):
        """
        检查用户名密码是否正确
        :param psw:
        :return:
        """
        md5_pwd = md5(psw.encode("utf-8")).hexdigest()
        if self.password != md5_pwd:
            return False
        return True

