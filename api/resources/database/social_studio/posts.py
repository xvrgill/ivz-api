from flask_restful import Resource
from flask import request
from pymongo.operations import UpdateOne
from api import mongo
from api.models.social_studio_post_schema import SocialStudioPostSchema
import json
from bson import json_util


class SocialStudioDBPosts(Resource):
    def post(self):
        """
        Update multiple Social Studio posts within the database if they exist.
        Create new Social Studio posts if they do not exist.
        """

        request_data = request.get_json()
        bulk_operations = []

        # Create bulk operations
        for post in request_data:
            deserialized = SocialStudioPostSchema().load(post)
            # Filter(match) by Air Table ID, set new values, enable upsert
            operation = UpdateOne(
                {"social_studio_id": deserialized["social_studio_id"]},
                update={"$set": {**deserialized}},
                upsert=True,
            )
            bulk_operations.append(operation)

        # Bulk write to collection
        result = mongo.db.socialStudioPosts.bulk_write(bulk_operations)

        # NOTE: Cannot serialize Object of type ObjectID - need to serialize then deserialize values
        response = json.loads(json.dumps(result.bulk_api_result, default=json_util.default))

        return response
