#imports
from flask import Flask, request
import werkzeug
import flask.scaffold

#setup
werkzeug.cached_property = werkzeug.utils.cached_property
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func


#Register API endpoints
from api_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.register_blueprint(documented_endpoint)



if __name__ == '__main__':
    print("***** Starting Mission Control ***** \n")
    app.run()
    

