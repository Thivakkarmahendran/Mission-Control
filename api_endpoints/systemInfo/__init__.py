from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('system_info', 'Systsem Info related endpoints')

system_info_model = namespace.model('SystemIndo', {
    'message': fields.String(
        readonly=True,
        description='system info message'
    )
})

System_info_example = {'message': 'System_Info!'}

@namespace.route('')
class systemInfo(Resource):

    @namespace.marshal_list_with(system_info_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''System Info message endpoint'''

        return System_info_example
    
    