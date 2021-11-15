from flask import Blueprint
from flask.json import jsonify
import requests
from api import mongo


collect_air_table_posts = Blueprint("collect_air_table_posts", __name__)
collect_social_studio_posts = Blueprint("collect_social_studio_posts", __name__)

# TODO: Maybe use abstract base class here?


@collect_air_table_posts.route("/db/air_table_posts/insert")
def store_air_table_posts():
    # Get Air Table posts from Air Table api
    response = requests.get("http://127.0.0.1:5000/api/air_table/posts")
    r = response.json()
    # Empty list too store response items
    updated_r = list()
    # List that stores only IDs from data pulled from API
    api_ids = list()

    # Extract fields and id from response. Store them in a new list for further processing.
    for post in r:
        field_data = post["fields"]
        _id = post["id"]
        field_data["id"] = _id
        updated_r.append(field_data)
        api_ids.append(_id)

    # Remove posts if they don't exist in Air Table api data but they do exist in our database

    # Get Air Table posts from database
    _cursor = mongo.db.airTablePosts.find({})
    existing_db_data = [x["air_table_id"] for x in _cursor]

    response_to_client = {
        "deleted_count": 0,
        "deleted_air_table_ids": [],
    }

    deleted_count = 0
    deleted_ids = []

    for _id in existing_db_data:
        if _id not in api_ids:
            # TODO: Return the ObjectID rather than the Air Table ID for uniformity
            # Remove that post from database
            _ = requests.delete(f"http://127.0.0.1:5000/db/air_table/post/{str(_id)}")
            deleted_count += 1
            deleted_ids.append(_id)

    response_to_client["deleted_count"] = deleted_count
    response_to_client["deleted_ids"] = deleted_ids

    # Add items in new list to database
    response2 = requests.post("http://127.0.0.1:5000/db/air_table/posts", json=updated_r).json()

    response_to_client["nMatched"] = response2["nMatched"]
    response_to_client["nModified"] = response2["nModified"]
    response_to_client["nUpserted"] = response2["nUpserted"]
    response_to_client["upserted"] = response2["upserted"]
    response_to_client["writeConcernErrors"] = response2["writeConcernErrors"]
    response_to_client["writeErrors"] = response2["writeErrors"]

    return jsonify(response_to_client)
