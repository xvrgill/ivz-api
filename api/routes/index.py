from flask import Blueprint, jsonify


index_page = Blueprint("index_page", __name__)


@index_page.route("/")
@index_page.route("/resources")
def index():
    """
    Give user a detailed list of resources for this api
    """
    resources = [
        {
            "name": "AirTablePosts",
            "uri": "/api/air_table/posts",
            "methods": {
                "GET": {
                    "description": "get air table posts from Air Table API",
                }
            },
        }
    ]

    return jsonify(resources)
