import json
from flask_restful import Resource
from flask import request, jsonify
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
        Create multiple Air Table posts within the database
        """

        request_data = request.get_json()
        insert_data = [AirTablePostSchema().load(x) for x in request_data]
        # deserialized = AirTablePostSchema().load(insert_data)
        result = mongo.db.airTablePosts.insert_many(insert_data)

        # Create new response object based on the result
        # NOTE: Cannot serialize Object of type InsertMany - need to pull out values
        response = {
            "acknowledged": result.acknowledged,
            # Serialize ObjectIDs to valid JSON string
            # Subsequently load valid JSON into a dictionary
            "insertedIds": json.loads(json.dumps(result.inserted_ids, default=json_util.default)),
        }

        return response
