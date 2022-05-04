#imports
from flask import Blueprint
from flask_restplus import Api

import METADATA
from api_endpoints.systemInfo import namespace as system_info_ns


blueprint = Blueprint('API_DOCS', __name__, url_prefix='')

api_extension = Api(
    blueprint,
    title = METADATA.APP_NAME,
    version = METADATA.VERSION,
    description = METADATA.DESCRIPTION,
    doc='/docs'
)

api_extension.add_namespace(system_info_ns)