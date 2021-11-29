from datetime import datetime
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


@collect_social_studio_posts.route("/db/social_studio_posts/insert")
def store_social_studio_posts():
    # Set default date range for the posts we'll collect
    # From date will always be January 1, 2021
    from_month = 1
    from_day = 1
    from_year = 2021
    # End date will always be current date
    current_date = datetime.now()
    current_month = int(current_date.strftime("%m"))
    current_day = int(current_date.strftime("%d"))
    current_year = int(current_date.strftime("%Y"))

    # Scrape Social Studio for existing posts by passing in dates defined above
    response = requests.get(
        f"http://127.0.0.1:5000/api/social_studio/posts?from_month={from_month}&from_day={from_day}&from_year={from_year}&to_month={current_month}&to_day={current_day}&to_year={current_year}"
    )

    # Get response as json
    r = response.json()
    updated_r = list()
    api_ids = list()

    # Extract data from response object
    for post in r:
        data = {
            "id": post["id"],
            "external_id": post["external_id"],
            "calendar_id": post["calendar_id"],
            "organization_id": post["organization_id"],
            "entity_type": post["entity_type"],
            "entity_class": post["entity_class"],
            "entity_id": post["entity_id"],
            "title": post["title"],
            "description": post["description"],
            "start_date": post["start_date"],
            "end_date": post["end_date"],
            "is_repeat": post["is_repeat"],
            "is_all_day": post["is_all_day"],
            "status": post["status"],
            "meta": post["meta"],
            "created": post["created"],
            "updated": post["updated"],
        }
        _id = post["id"]
        updated_r.append(data)
        api_ids.append(_id)

    # Get Social Studio posts from database
    _cursor = mongo.db.socialStudioPosts.find({})
    existing_db_data = [x["social_studio_id"] for x in _cursor]

    response_to_client = {
        "deleted_count": 0,
        "deleted_social_studio_ids": [],
    }

    deleted_count = 0
    deleted_ids = []

    for social_studio_id in existing_db_data:
        if social_studio_id not in api_ids:
            # TODO: Return the ObjectID rather than the Air Table ID for uniformity
            # Remove that post from database
            _ = requests.delete(
                f"http://127.0.0.1:5000/db/social_studio/post/{str(social_studio_id)}"
            )
            deleted_count += 1
            deleted_ids.append(social_studio_id)

    response_to_client["deleted_count"] = deleted_count
    response_to_client["deleted_ids"] = deleted_ids

    response2 = requests.post("http://127.0.0.1:5000/db/social_studio/posts", json=updated_r).json()

    response_to_client["nMatched"] = response2["nMatched"]
    response_to_client["nModified"] = response2["nModified"]
    response_to_client["nUpserted"] = response2["nUpserted"]
    response_to_client["upserted"] = response2["upserted"]
    response_to_client["writeConcernErrors"] = response2["writeConcernErrors"]
    response_to_client["writeErrors"] = response2["writeErrors"]

    return jsonify(response_to_client)
