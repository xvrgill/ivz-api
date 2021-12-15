from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
mongo = PyMongo(app)
api = Api(app)
CORS(app)

# Import blueprints


# Register blueprints


# Resource imports
from api.resources.social_studio import SocialStudio

# Resource definitions
api.add_resource(SocialStudio, "/socialstudio/post/<string:id>")
