import json
from flask_restful import Resource
from flask import request
from pymongo.operations import UpdateOne

# from pymongo.operations import UpdateOne
from api import mongo
from api.models.air_table_post_schema import AirTablePostSchema
from bson import json_util


class AirTableDBPosts(Resource):
    def get(self):
        """
        Retrieve multiple Air Table posts from the database
        """

        # Iterate over args to create new dict (request.args is immutable)
        query = {k: v for k, v in request.args.items()}

        # Change bool strings to boolean data type (query will not return results if in string format)
        if "true" or "false" in query:
            value = bool(query["email_trigger"])
            query["email_trigger"] = value

        # Query the database with our modified dictionary of parameters
        result = mongo.db.airTablePosts.find(query)
        # Iterate over the cursor to get a list of bson docs
        _bson = [doc for doc in result]
        # Serialize bson data manually using json_util (ObjectID is not json serializable by default)
        serialized = json.dumps(_bson, default=json_util.default)

        # Return deserialized data (turns json data into dictionary)
        return json.loads(serialized)

    def post(self):
        """
        Update multiple Air Table posts within the database if they exist.
        Create new Air Table posts if they do not exist.
        """

        request_data = request.get_json()
        bulk_operations = []

        # Create bulk operations
        for post in request_data:
            deserialized = AirTablePostSchema().load(post)
            # Filter(match) by Air Table ID, set new values, enable upsert
            operation = UpdateOne(
                {"air_table_id": deserialized["air_table_id"]},
                update={"$set": {**deserialized}},
                upsert=True,
            )
            bulk_operations.append(operation)

        # Bulk write to collection
        result = mongo.db.airTablePosts.bulk_write(bulk_operations)

        # NOTE: Cannot serialize Object of type ObjectID - need to serialize then deserialize values
        response = json.loads(json.dumps(result.bulk_api_result, default=json_util.default))

        return response
