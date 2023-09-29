from flask_restful import Resource
from flask import session

class Logout(Resource):
    def delete(self):
        # Remove the user_id value from the session
        session.pop('user_id', None)
        return '', 204
