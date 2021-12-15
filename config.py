from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class DevelopmentConfig:
    # Set config variables
    # FLASK_APP = "api"
    # FLASK_ENV = "development"
    # TESTING = True
    SECRET_KEY = environ.get("SECRET_KEY")
    # STATIC_FOLDER = "static"
    # TEMPLATES_FOLDER = "templates"

    # Database
    MONGO_URI = environ.get("ATLAS_CONNECTION_STRING")

    # Air Table API
    AIR_TABLE_API_KEY = environ.get("AIR_TABLE_API_KEY")
    AIR_TABLE_BASE_ID = environ.get("AIR_TABLE_BASE_ID")
    AIR_TABLE_TABLE_NAME = environ.get("AIR_TABLE_TABLE_NAME")

    # AWS Secrets
    # AWS_SECRET_KEY = environ.get("AWS_SECRET_KEY")
    # AWS_KEY_ID = environ.get("AWS_KEY_ID")


# Production Configuration
class ProductionConfig:
    pass
