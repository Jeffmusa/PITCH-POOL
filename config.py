import os



class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vicklyne:Moringa123@localhost/pitch'



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vicklyne:Moringa123@localhost/pitch'
    DEBUG = True    

class ProdConfig(Config):
    pass    


config_options={
    'development':DevConfig,
    'production': ProdConfig
}
