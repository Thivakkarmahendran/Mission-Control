from flask import Blueprint, request

blueprint = Blueprint('runApp', __name__, url_prefix='/runApp')

@blueprint.route('/run')
def runApplication():
    return {
        'message': "Running Application",
    }