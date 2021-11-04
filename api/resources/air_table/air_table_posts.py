import os
from flask_restful import Resource
from pyairtable import Table

api_key = os.environ.get("AIR_TABLE_API_KEY")
base_id = os.environ.get("AIR_TABLE_BASE_ID")
table_name = os.environ.get("AIR_TABLE_TABLE_NAME")

# return list of all entries
class AirTablePosts(Resource):
    def get(self):
        table = Table(api_key, base_id, table_name)
        return table.all()
