from flask_restful import Resource
from flask import request
from api import mongo
import json
from bson import json_util


class SocialStudioDBPost(Resource):
    def get(self, id):
        """
        Get single Air Table post from the Air Table collection within the database.
        """

        # TODO: Deserialize this data before returning it
        result = mongo.db.socialStudioPosts.find_one({"_id": id})

        return result

    def put(self, id):
        """
        Update an existing singlular Air Table post within the Air Table collection within the database.
        """

        data = request.get_json()
        result = mongo.db.socialStudioPosts.update_one({"_id": id}, {"$set": data})

        return result

    def delete(self, id):
        """
        Delete single Air Table post from the Air Table collection within the database.
        """

        result = mongo.db.socialStudioPosts.delete_one({"social_studio_id": int(id)})
        result = json.loads(json.dumps(result.raw_result, default=json_util.default))

        return result
