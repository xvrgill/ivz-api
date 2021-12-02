from flask import Blueprint
from flask.json import jsonify
from pymongo import cursor
import requests
from api import mongo
import json
from bson import json_util


create_db_relationships = Blueprint("create_db_relationships", __name__)


@create_db_relationships.route("/db/link_posts")
def link():

    # Create object to store linked posts
    updated_posts = list()

    # Get social studio posts from database
    ss_cursor: cursor.Cursor = mongo.db.socialStudioPosts.find({})
    ss_posts: list = [json.loads(json.dumps(x, default=json_util.default)) for x in ss_cursor]

    # For every post in social studio collection...
    for post in ss_posts:
        # Turn id into object id
        _id: str = post["_id"]["$oid"]
        # oid: ObjectId = ObjectId(_id)
        ss_copy: str = post["description"]

        if ss_copy:
            pipeline = [
                {
                    "$search": {
                        "index": "default",
                        "text": {
                            "query": ss_copy,
                            "path": {"wildcard": "*"},
                        },
                    }
                },
                {"$project": {"score": {"$meta": "searchScore"}}},
                {"$limit": 1},
                {
                    "$lookup": {
                        "from": "airTablePosts",
                        "localField": "_id",
                        "foreignField": "_id",
                        "as": "air_table_record",
                    }
                },
                {
                    "$project": {
                        # "new_social_studio_oid": _id,
                        # "score": "$score",
                        "air_table_id": "$air_table_record.air_table_id",
                        "linked_social_studio_ids": {
                            "$map": {
                                "input": "$air_table_record",
                                "as": "record",
                                "in": "$$record.linked_social_studio_ids",
                            }
                        },
                    }
                },
            ]

            for doc in mongo.db.airTablePosts.aggregate(pipeline):
                search_result = json.loads(json.dumps(doc, default=json_util.default))
                if search_result != None:
                    existing_linked_posts = search_result["linked_social_studio_ids"]
                    search_result["air_table_id"] = search_result["air_table_id"][0]
                    if existing_linked_posts != [None]:
                        if _id not in existing_linked_posts:
                            existing_linked_posts.append(_id)
                            search_result.update(
                                {"linked_social_studio_ids": existing_linked_posts}
                            )
                    else:
                        existing_linked_posts = list()
                        existing_linked_posts.append(_id)
                        search_result.update({"linked_social_studio_ids": existing_linked_posts})

                    data = {
                        "id": search_result["air_table_id"],
                        "linked_social_studio_ids": search_result["linked_social_studio_ids"],
                    }

                    # TODO: Need to update db in the for loop incase two social studio posts match a single air table record
                    updated_posts.append(data)

    # TODO: Update Air Table posts with http requests - need to do this inside the for loop for each update
    response = requests.post("http://127.0.0.1:5000/db/air_table/posts", json=updated_posts).json()

    return jsonify(response)
