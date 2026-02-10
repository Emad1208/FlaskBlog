import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')    



class Development(Config):
    DEBUG = True
    



class Production(Config):
    DEBUG = False





