
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some secret'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:data@*0418@127.0.0.1:5432/july_payroll'
    environment = 'Developmet'
    DEBUG = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:data@*0418@127.0.0.1:5432/july_payroll'
    environment = 'Developmet'
    DEBUG = True

class Testing(Config):
    #SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://ctpjkgbceszgun:0ae8b5c5e8cfc16245878c66f0cfe275b8ad78ebbb7a5d1c22e0828716b6e68b@ec2-54-221-215-228.compute-1.amazonaws.com:5432/dfq0lifq3j8974'
    DEBUG = False
    # environment = 'Production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False