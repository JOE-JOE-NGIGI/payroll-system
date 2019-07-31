
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
    environment = 'Production'