from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure to set your secret key

@app.route('/login', methods=['POST'])
def login():
    # Your login logic here
    # ...

    # Return a JSON response with the user data
    response_data = {'message': 'Login successful', 'user_id': user_id}
    return jsonify(response_data), 200
