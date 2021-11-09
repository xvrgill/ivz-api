from flask import Blueprint
from flask.json import jsonify
import requests


collect_air_table_posts = Blueprint("collect_air_table_posts", __name__)
collect_social_studio_posts = Blueprint("collect_social_studio_posts", __name__)

# TODO: Maybe use abstract base class here?


@collect_air_table_posts.route("/db/air_table_posts/insert")
def store_air_table_posts():
    # Get Air Table posts from Air Table api
    response = requests.get("http://127.0.0.1:5000/api/air_table/posts")
    r = response.json()
    # Extract fields and id from response. Store them in a new list for further processing.
    updated_r = list()
    for post in r:
        field_data = post["fields"]
        _id = post["id"]
        field_data["id"] = _id
        updated_r.append(field_data)

    # Add items in new list to database
    response2 = requests.post("http://127.0.0.1:5000/db/air_table/posts", json=updated_r).json()

    return jsonify(response2)
