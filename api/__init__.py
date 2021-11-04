from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api


app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
api = Api(app)
CORS(app)

# Import blueprints
from api.routes.index import index_page
from api.routes.collect_posts import collect_air_table_posts

# Register blueprints
app.register_blueprint(index_page)
app.register_blueprint(collect_air_table_posts)

# Resource imports
from api.resources.air_table.air_table_posts import AirTablePosts
from api.resources.air_table.air_table_post import AirTablePost
from api.resources.air_table.filtered_air_table_posts import FilteredAirTablePosts
from api.resources.social_studio.social_studio_posts import SocialStudioPosts
from api.resources.database.air_table.post import AirTableDBPost
from api.resources.database.air_table.posts import AirTableDBPosts

# Resource definitions
api.add_resource(AirTablePosts, "/api/air_table/posts")
api.add_resource(AirTablePost, "/api/air_table/post/<string:post_id>")
api.add_resource(FilteredAirTablePosts, "/api/air_table/filtered_posts")
api.add_resource(SocialStudioPosts, "/api/social_studio/posts")
api.add_resource(AirTableDBPost, "/db/air_table/post/<string:id>")
api.add_resource(AirTableDBPosts, "/db/air_table/posts")
