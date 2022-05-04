#imports
from flask import Blueprint
from flask_restplus import Api

import METADATA
from api_endpoints.application import namespace as applicationNS


blueprint = Blueprint('API_DOCS', __name__, url_prefix='')

api_extension = Api(
    blueprint,
    title = METADATA.APP_NAME,
    version = METADATA.VERSION,
    description = METADATA.DESCRIPTION,
    doc='/docs'
)

api_extension.add_namespace(applicationNS)