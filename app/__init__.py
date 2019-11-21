from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__, url_prefix="/api/documentation")

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='FLASK RESTPLUS API WITH JWT',
          version='1.0',
          description='a flask restplus web service',
          authorizations=authorizations
          )

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(auth_ns, path='/api')
