import os
from flask_restful import Resource, request, abort
from pyairtable import Table
from api.models.filter_query import FilterQuerySchema
from marshmallow import ValidationError


api_key = os.environ.get("AIR_TABLE_API_KEY")
base_id = os.environ.get("AIR_TABLE_BASE_ID")
table_name = os.environ.get("AIR_TABLE_TABLE_NAME")


# return list of all entries filtered with a formula
class FilteredAirTablePosts(Resource):
    def get(self):
        table = Table(api_key, base_id, table_name)

        # validate url parameters
        args = request.args
        try:
            result = FilterQuerySchema().load(args)
        except ValidationError as err:
            return err.messages, 400

        # create dictionary for filtered fields
        filter_field_data = dict()

        f_by = f"{{{result['filter_by']}}}"
        f_type = result["filter_type"]
        filter_field_data.update({"f_by": f_by})
        filter_field_data.update({"f_type": f_type})
        if "search_string" in result:
            s_string = result["search_string"]
            filter_field_data.update({"s_string": s_string})

        # create formulas from passed url parameters

        # if filter type is 'contains', create a 'find' formula
        # raise error if filter type is unsupported
        if filter_field_data["f_type"] == "contains":
            # abort if search string doesn't exist
            if "s_string" not in filter_field_data:
                return abort(405, message="search string not supplied")
            formula = f"FIND('{filter_field_data['s_string']}', ARRAYJOIN({filter_field_data['f_by']}))"
            return table.all(formula=formula)
        else:
            return abort(405, message="unsupported filter type used")
