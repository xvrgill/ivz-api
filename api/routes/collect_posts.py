from flask import Blueprint
from flask.json import jsonify
import requests


collect_air_table_posts = Blueprint("collect_air_table_posts", __name__)
collect_social_studio_posts = Blueprint("collect_social_studio_posts", __name__)

# TODO: Maybe use abstract base class here?


@collect_air_table_posts.route("/db/air_table_posts/insert")
def store_air_table_posts():
    # Get Air Table posts from Air Table api
    _response = requests.get("http://127.0.0.1:5000/api/air_table/posts")
    r = _response.json()
    # Extract fields and id from response in reformatted dict
    final_response = list()
    for post in r:
        field_data = post["fields"]
        _id = post["id"]
        field_data["id"] = _id
        final_response.append(field_data)

    # TODO: Serialize all posts
    # TODO: Add them to database
    return jsonify(final_response)
