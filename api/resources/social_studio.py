from flask_restful import Resource, abort
from flask import request, jsonify
from api.refactored.exceptions import RegexPatternResultError, StrategyNotSupportedError
import requests
from api.refactored.at_api_controller import AirTableApiController
from api.refactored.at_schema import AirTablePostSchema
from api.refactored.post import SocialStudioPostContext


class SocialStudio(Resource):
    def get(self, id: str):
        """
        Method that allows for get request to be processed by the API.
        Air Table constraints require a get request to be sent from client.
        Accepts data as parameters, processes the data, and posts it the the associated post route.
        """

        # Get data from Air Table API
        controller = AirTableApiController()
        airtable_api_result = controller.get_record(id)
        result_fields = airtable_api_result["fields"]

        # Deserialize field data
        schema = AirTablePostSchema()
        deserialized_result = schema.load(result_fields)
        deserialized_result["air_table_id"] = id

        # Serialize data to pass to post method
        serialized_result = schema.dumps(deserialized_result)

        # Pass data to post method to add to social studio
        post_response = requests.post(f"{request.url_root}socialstudio/post/{id}", json=serialized_result)

        return post_response.json()

    def post(self, id):
        """
        Creates new post in social studio.
        """
        id: str = id

        # Implement social studio context
        data = request.json
        schema: AirTablePostSchema = AirTablePostSchema()
        deserialized_data = schema.loads(data)
        response_data: dict = {"posts_created": 0, "created_posts": {}}

        if len(deserialized_data["social_channel"]) < 1:
            # Raise error
            raise ValueError("No social channel(s) selected in Air Table")

        social_channel_list = [x.lower() for x in deserialized_data["social_channel"]]

        # TODO: Create logic that enables the use of different brand strategies for each platform (eg. US Retail, CA Retail, US Institutional)
        if "linkedin" in social_channel_list:
            try:
                # Initialize post context. Pass deserialized data and platform as string
                ssc = SocialStudioPostContext(deserialized_data, "linkedin")
                # Run context processing and store return values to add to final response
                parsed_copy, image_path, draft_url, draft_id = ssc.run()

                # Assemble response to be passed back to the client
                response_data["posts_created"] += 1
                response_details: dict = {"us retail": {"copy": parsed_copy, "image_path": image_path, "draft_url": draft_url, "draft_id": draft_id}}
                response_data["created_posts"].update({"linkedin": [response_details]})

            #  Handle lower level errors
            except RegexPatternResultError as e:
                abort(422, error=f"{e.message}")
            except StrategyNotSupportedError as e:
                abort(400, error=f"{e.message}")
            return jsonify(response_data)
        else:
            try:
                raise ValueError()
            except ValueError:
                abort(400, message="linkedin not included in social channels selection in Air Table")
