import os

class AppConfig:

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', "data/files/")

    SECRET_KEY = os.urandom(32)

    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Enable debug mode.
    DEBUG = False

    # Connect to the database
    SQLALCHEMY_DATABASE_URI = os.getenv('APP_DB', 'sqlite:///data/databases/binarapi_db.sqlite')

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Settings:
    JWT_SECRET = os.getenv('JWT_SECRET', 'QWERTYhgfdsaZXCVB%$#@!12345')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256') 

class Telegram:
    TOKEN = os.getenv('TOKEN_TELEGRAM', '5537689921:AAED4cMDNOem654t1wG2j70gVNo6YqIy_5o11') 
    CHAT_ID = os.getenv('CHAT_ID_TELEGRAM', '52026454711') 