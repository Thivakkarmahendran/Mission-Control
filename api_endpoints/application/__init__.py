from flask import request
from flask_restplus import Namespace, Resource, fields
import METADATA

namespace = Namespace('Application', 'Mission Control related endpoints')


@namespace.route("/name")
@namespace.doc(responses={200: "OK", 400: 'Invalid Argument', 500: 'Error Processing'})
class appName(Resource):
    def get(self):
        """
        returns the App Name
        """
        return METADATA.APP_NAME
        
        
@namespace.route("/version")
@namespace.doc(responses={200: "OK", 400: 'Invalid Argument', 500: 'Error Processing'})
class appVersion(Resource):
    def get(self):
        """
        returns the App Version
        """
        return METADATA.VERSION
    
@namespace.route("/description")
@namespace.doc(responses={200: "OK", 400: 'Invalid Argument', 500: 'Error Processing'})
class appDescription(Resource):
    def get(self):
        """
        returns the App Description
        """
        return METADATA.DESCRIPTION


""" Model for new user """
userData = namespace.model('Add new show',{
    "fname" : fields.String(description="First Name", required=True),
    "lname" : fields.String(description="Last Name", required=True),
    "age" : fields.Integer(description="Age", required=True),
    "male" : fields.Boolean(description="Male?", required=True),
})

@namespace.route("/testUser")
class appDescription(Resource):
    @namespace.expect(userData)
    @namespace.doc(responses={200: "OK", 400: 'Invalid Argument', 500: 'Error Processing'})
    def put(self):
        """
        returns the App Description
        """
        print(request.json)
        return
