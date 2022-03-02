import os
# os module will allow our application to interact with the
# operating system

class Config:
    """
    Config class will contain all(general) configurations/optimization
    that will will be used in Development stage and Production class.
    """ 
    NEWS_API_BASE_URL ='http://newsapi.org/v2/everything?q={}&from=2021-01-22&sortBy=publishedAt&apiKey={}'
    ARTICLE_API_BASE_URL ='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):
        pass    

class ProdConfig(Config):
    """    
    This sub-class will also contain all the other configurations to
    facilitate the production class. 
    Args:
        Config: This sub-class will inherit all configurations from Config, base class.
    """
    pass


class DevConfig(Config):
    """
    Sub-class contains all configurations that will facilate the development stage.
    
    Args:
        Config: Sub-class also inherits all the configurations from Config, base-class.        
    """
    # To enable debug mode.
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
