from datetime import datetime
from flask import Blueprint
from flask.json import jsonify
import requests
from api import mongo


create_db_relationships = Blueprint("create_db_relationships", __name__)


@create_db_relationships.route("/db/air_table_posts/insert")
def link():

    # Create object to store linked posts

    # For every post in social studio collection...
    # Search for a matching air table post by comparing copy
    # If one is found...
    # Copy air table post data into a python object
    # If linked posts field is in keys...
    # If social studio object id does not exist in this list...
    # Update linked posts list with social studio object id
    # Else...
    # Add linked posts field with a list that contains the social studio id
    # Append new object to storage object

    # Bulk update Air Table posts with http request

    pass
