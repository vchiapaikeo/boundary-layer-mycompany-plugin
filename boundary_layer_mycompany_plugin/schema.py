import marshmallow as ma

from boundary_layer.schemas.base import StrictSchema


class MyCompanyPluginConfigSchema(StrictSchema):
    some_key = ma.fields.String()
