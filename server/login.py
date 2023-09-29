from flask_restful import Resource, reqparse, abort
from flask import session, jsonify
from models import User  # Import your User model from your project

class Login(Resource):
    def post(self):
        # Parse the username from the request JSON
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        args = parser.parse_args()

        # Retrieve the user by username (assuming it's unique)
        user = User.query.filter_by(username=args['username']).first()

        if user:
            # Set the session's user_id value to the user's id
            session['user_id'] = user.id
            return jsonify(user), 200
        else:
            abort(401, message="Unauthorized")
