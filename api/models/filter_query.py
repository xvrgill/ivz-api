from marshmallow import Schema, fields


class FilterQuerySchema(Schema):
    filter_by = fields.Str(required=True)
    filter_type = fields.Str(required=True)
    search_string = fields.Str()
