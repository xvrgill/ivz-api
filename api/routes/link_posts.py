from flask import Blueprint
from flask.json import jsonify
from pymongo import cursor
from api import mongo
import json
from bson import json_util
from bson.objectid import ObjectId


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

        # Search for a matching air table post by comparing copy
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
                {"$project": {"social_studio_oid": _id, "score": {"$meta": "searchScore"}}},
                {"$limit": 1},
            ]

            for doc in mongo.db.airTablePosts.aggregate(pipeline):
                updated_posts.append(json.loads(json.dumps(doc, default=json_util.default)))

            # # If one is found...
            # if search_result != None:
            #     # If linked posts field is in keys... (check if field exists)
            #     if "linked_social_studio_ids" in search_result_dict.keys():
            #         # If social studio object id does not exist in this list... (check if id exists)
            #         if _id in search_result_dict["linked_social_studio_ids"]:
            #             # Append social studio object id to list
            #             search_result_dict["linked_social_studio_ids"].append(_id)
            #     else:
            #         # Add linked posts field with a list that contains the social studio id
            #         search_result_dict["linked_social_studio_ids"] = [_id]

            # # Append new object to storage object
            # updated_posts.append(search_result_dict)

    # Bulk update Air Table posts with http request

    return jsonify(updated_posts)
