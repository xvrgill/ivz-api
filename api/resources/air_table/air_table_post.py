import os
from flask_restful import Resource
from pyairtable import Table

api_key = os.environ.get("AIR_TABLE_API_KEY")
base_id = os.environ.get("AIR_TABLE_BASE_ID")
table_name = os.environ.get("AIR_TABLE_TABLE_NAME")


class AirTablePost(Resource):
    def get(self, post_id):
        """
        returns single air table entry
        """

        table = Table(api_key, base_id, table_name)
        first_result = table.get(post_id)

        return first_result

    def post(self, post_id):
        """
        creates a single new air table entry.
        returns post data, success message, and status code
        """
        return {"air table post": f"post success {post_id}"}

    def put(self, post_id):
        """
        updates a single air table entry.
        returns updated entry, success message, and status code
        """
        return {"air table put": f"put success {post_id}"}

    def delete(self, post_id):
        """
        deletes single air table entry.
        returns deleted entry id, success message, and status code
        """
        return {"air table delete": f"delete success {post_id}"}
