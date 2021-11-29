from marshmallow import Schema, fields


class SocialStudioPostSchema(Schema):
    _id = fields.String()
    social_studio_id = fields.Int(data_key="id")
    external_id = fields.Str()
    calendar_id = fields.Str()
    organization_id = fields.Str()
    entity_type = fields.Int()
    entity_class = fields.Int()
    entity_id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    publish_date = fields.Str(data_key="start_date")
    end_date = fields.Str()
    is_repeat = fields.Bool()
    is_all_day = fields.Bool()
    status = fields.Int()
    meta = fields.Dict()
    created = fields.Str()
    updated = fields.Str()
