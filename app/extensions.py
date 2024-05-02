from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_restx import Api, abort

from flask_migrate import Migrate

api = Api()
db = SQLAlchemy()
migrate = Migrate()

from flask import request, jsonify
from functools import wraps 

def require_apikey(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key or api_key != 'PN9AbvdtzEBcR1bhuqTfFFbTU846xG3n':
            abort(403, 'API key required')
        return func(*args, **kwargs)
    return decorated

