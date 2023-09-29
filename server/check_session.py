from flask_restful import Resource, abort
from flask import session, jsonify
from models import User  # Import your User model from your project

class CheckSession(Resource):
    def get(self):
        # Retrieve the user_id value from the session
        user_id = session.get('user_id')

        if user_id:
            # If the session has a user_id, return the user as JSON
            user = User.query.get(user_id)
            return jsonify(user), 200
        else:
            # If the session does not have a user_id, return 401 (Unauthorized)
            abort(401, message="Unauthorized")
