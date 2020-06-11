class Config(object):
    """
    Configurações comuns
    """


class ConfigDevelopment(Config):
    DEBUG = True
    SQLALCHEMY_ECHO= True

class ConfigProduction(Config):
    DEBUG = False


app_config = {
    'development' : ConfigDevelopment,
    'production' : ConfigProduction 
}